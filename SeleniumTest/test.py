import json
import time
import csv

import pytest
import pytest_check
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


BASE_URL = "https://www.glassdoor.com/Salaries/index.htm"
SWE_URL = "https://www.glassdoor.com/Salary/Google-Software-Engineer-Salaries-E9079_D_KO7,24_P1.htm"

def test_select_job_title():
    driver = webdriver.Chrome()

    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "HeroSearch_inputContainer__I2kuw")))

    title_input = driver.find_element(By.CLASS_NAME, "HeroSearch_keywordInputContainer__BTfou")
    actions.move_to_element(title_input).click().send_keys("Software Engineer").perform()
    
       
    element = driver.find_element(By.CLASS_NAME, "HeroSearch_searchIcon__m_V6X")
    actions.move_to_element(element).click().perform()
    time.sleep(2)
    
    wait.until(EC.url_contains ("/software-engineer-salary"))
    pytest_check.is_true(EC.url_contains ("/software-engineer-salary"))
    
    driver.quit()


def test_get_salary_data():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    driver.get(SWE_URL)
    
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "individualsalaries_IndividualSalariesTable__4PdiK")))
        table = driver.find_element(By.CLASS_NAME, "individualsalaries_IndividualSalariesTable__4PdiK")
        
        rows = table.find_elements(By.TAG_NAME, "tr")
        data = []
        for row in rows:
            headers = row.find_elements(By.TAG_NAME, "th")
            headers = [ele.text.strip() for ele in headers]
            data.append([ele for ele in headers if ele])
            cols = row.find_elements(By.TAG_NAME, "td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
            
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    finally:
        driver.quit()



def convert_output_to_data():
    input_file = '../SeleniumTest/output.csv'
    output_file = '../SeleniumTest/converted_output.csv'

# Open the input and output files
    with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
        # Create a CSV reader and writer objects
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)

        # Write the header row to the output file
        writer.writerow(['JobTitle', 'Location', 'TotalPay', 'Base', 'Bonus', 'Stock', 'YearsofExperience', 'DateSubmitted'])

        # Skip the first row (header) in the input file
        next(reader)

        # Process each row in the input file
        for row in reader:
            # Extract the required fields from the input row
            job_title = row[0].split('\n')[0]
            location = row[0].split('\n')[1]
            total_pay = row[1].split('\n')[0]
            base = row[1].split('\n')[1].split('|')[0].strip()
            bonus = row[1].split('\n')[1].split('|')[1].strip()
            stock = row[1].split('\n')[1].split('|')[2].strip()
            years_of_experience = row[2]
            date_submitted = row[3].strip('"')

            # Write the processed row to the output file
            writer.writerow([job_title, location, total_pay, base, bonus, stock, years_of_experience, date_submitted])

    print("Conversion completed successfully.")
    

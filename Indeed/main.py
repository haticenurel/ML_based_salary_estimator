import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv

counter = 0
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# driver.get("https://tr.indeed.com/jobs?q=software+engineer&l=&from=searchOnHP&vjk=f6d4255c7c86f892")
driver.get("https://de.indeed.com/jobs?q=Softwareentwickler&l=&from=searchOnDesktopSerp&vjk=c56ccb62238add2c")
# driver.get("https://nl.indeed.com/jobs?q=software+engineering&l=&from=searchOnDesktopSerp&vjk=60742e40404e380e")

# csv init part
filename = "nl_salaries.csv"
fields = ["id","name","salary","location","work-type"]
rows = []

hasMorePage = True
time.sleep(100)
while hasMorePage:
    time.sleep(random.random()*15)
    job_headings_list = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-zu9cdh')))[0]
    job_headings = job_headings_list.find_elements(By.CSS_SELECTOR, "#mosaic-provider-jobcards > ul > li")

    print(job_headings)
    for heading in job_headings:
        try:
            clickable_part = heading.find_element(By.TAG_NAME, 'a')
            clickable_part.click()
            time.sleep(random.random()*5)
            try:
                targetJobDesc = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fastviewjob")))
                targetInfo = targetJobDesc[0].find_element(By.ID, "salaryInfoAndJobType")
                targetSalary = targetJobDesc[0].find_elements(By.CLASS_NAME, "css-19j1a75")
                targetLocation = targetJobDesc[0].find_elements(By.CLASS_NAME, "css-waniwe")
                targetJobTitle = targetJobDesc[0].find_elements(By.CLASS_NAME, "jobsearch-JobInfoHeader-title")
                # targetLocation = targetJobDesc[0].find_elements(By.CLASS_NAME, "css-k5flys")
                targetType = targetJobDesc[0].find_elements(By.CLASS_NAME, "js-match-insights-provider-g6kqeb")
                if targetSalary:
                    counter += 1
                    jobtitle = targetJobTitle[0].text.replace("\n","")
                    newData = [counter,jobtitle,targetSalary[0].text]
                    print(targetSalary[0].text)
                    if len(targetLocation)>0:
                        print(targetLocation[0].text)
                        newData.append(str(targetLocation[0].text))
                    else:
                        newData.append("NULL")
                    if len(targetType):
                        print(targetType[1].text)
                        newData.append(targetType[1].text)
                    else:
                        newData.append("NULL")
                    print(counter)
                    rows.append(newData)
                    print(rows)
            except NoSuchElementException:
                print("ERRRRRRRRRRRRRROR.")


        except NoSuchElementException:
            print("Clickable part not found in this job heading.")
        print("-----------------------------")


    nextBtnL = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#jobsearch-JapanPage > div > div.css-hyhnne.e37uo190 > div > div.css-pprl14.eu4oa1w0 > nav > ul > li:last-child > a')))
    try:
        nextBtn = nextBtnL[0]
        print(nextBtn)
        time.sleep(2)
        nextBtn.click()
        time.sleep(5)
    except:
        print("************************************************************************************************************")
        print("end of the Pages")
        print("************************************************************************************************************")
        hasMorePage = False

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
        print(rows)
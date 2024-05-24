import pandas as pd
import re 
import numpy as np

#read final.csv data
dataframe1 = pd.read_csv('final.csv')


# Remove first column
dataframe1 = dataframe1.iloc[:, 1:]

dataframe1.loc[dataframe1["city"] == "İstanbul", "city"] = 1
dataframe1.loc[dataframe1["city"] == "34 İstanbul", "city"] = 1
#istanbul ve 34 istanbul aynı şehir olduğu için 1 olarak işaretlendi bunların dışındaki şehirler 0 olarak işaretlendi
dataframe1.loc[dataframe1["city"] != 1, "city"] = 0

dataframe1.loc[dataframe1["currency"].str.contains("Türk Lirası"), "currency"] = 1
#if currency is other than Turkish Lira, and salary is not end with TL, I need to convert them to dolar
dataframe1.loc[(dataframe1["currency"].str.contains("Dolar") | dataframe1["currency"].str.contains("Euro") | dataframe1["currency"].str.contains("Sterlin")) & dataframe1["salary"].str.contains("TL"), "currency"] = 1

dataframe1.loc[dataframe1["level"] == "Yeni mezun", "level"] = 1
dataframe1.loc[dataframe1["level"] == "Junior", "level"] = 1
dataframe1.loc[dataframe1["level"] == "Middle", "level"] = 2
dataframe1.loc[dataframe1["level"] == "Mid", "level"] = 2
dataframe1.loc[dataframe1["level"] == "Senior", "level"] = 3

dataframe1.loc[dataframe1["experience"] == "0 - 1 Yıl", "experience"] = 1
dataframe1.loc[dataframe1["experience"] == "0-1 Yıl", "experience"] = 1
dataframe1.loc[dataframe1["experience"] == "1-3 Yıl", "experience"] = 2
dataframe1.loc[dataframe1["experience"] == "1 - 3 Yıl", "experience"] = 2
dataframe1.loc[dataframe1["experience"] == "3-5 Yıl", "experience"] = 3
dataframe1.loc[dataframe1["experience"] == "3 - 5 Yıl", "experience"] = 3
dataframe1.loc[dataframe1["experience"] == "5 - 7 Yıl", "experience"] = 4
dataframe1.loc[dataframe1["experience"] == "5-7 Yıl", "experience"] = 4
dataframe1.loc[dataframe1["experience"] == "7-9 Yıl", "experience"] = 5
dataframe1.loc[dataframe1["experience"] == "7 - 10 Yıl", "experience"] = 5
dataframe1.loc[dataframe1["experience"] == "10-12 Yıl", "experience"] = 6
dataframe1.loc[dataframe1["experience"] == "10 - 12 Yıl", "experience"] = 6
dataframe1.loc[dataframe1["experience"] == "9-12 Yıl", "experience"] = 6
dataframe1.loc[dataframe1["experience"] == "12-14 Yıl", "experience"] = 7
dataframe1.loc[dataframe1["experience"] == "12 - 14 Yıl", "experience"] = 7
dataframe1.loc[dataframe1["experience"] == "12 Yıl ve üzeri", "experience"] = 8
dataframe1.loc[dataframe1["experience"] == "15 Yıl ve üzeri", "experience"] = 8




dataframe1.loc[dataframe1["work_type"] == "Ofis", "work_type"] = 1
dataframe1.loc[dataframe1["work_type"] == "Ofiste", "work_type"] = 1
dataframe1.loc[dataframe1["work_type"] == "Hibrit", "work_type"] = 2
dataframe1.loc[dataframe1["work_type"] == "Hybrid", "work_type"] = 2
dataframe1.loc[dataframe1["work_type"] == "Şu an hibrit ama ofise döneceğiz.", "work_type"] = 2
dataframe1.loc[dataframe1["work_type"] == "Hibrit (Ofis + Remote)", "work_type"] = 3
dataframe1.loc[dataframe1["work_type"] == "Şu an remote ama hibrite döneceğiz.", "work_type"] = 3
dataframe1.loc[dataframe1["work_type"] == "Remote", "work_type"] = 3


dataframe1['office'] = np.where(dataframe1['work_type'] == 1, 'yes', 'no')
dataframe1['hybrid'] = np.where(dataframe1['work_type'] == 2, 'yes', 'no')
dataframe1['remote'] = np.where(dataframe1['work_type'] == 3, 'yes', 'no')

#remove work_type column
dataframe1.drop(['work_type'], axis=1, inplace=True)

#if company size is not specified or contains no text or number, it is assumed to be 0    
dataframe1.loc[dataframe1["company_size"].isnull() | (dataframe1["company_size"] == ""), "company_size"] = 0
dataframe1.loc[dataframe1["company_size"] == "1 - 5 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "1-10", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "6 - 10 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "11-20", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "11 - 20 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "21-50", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "21 - 50 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "51-150", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "51 - 100 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "101 - 249 Kişi", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "250+", "company_size"] = 1
dataframe1.loc[dataframe1["company_size"] == "151-300", "company_size"] = 2
dataframe1.loc[dataframe1["company_size"] == "301-600", "company_size"] = 2
dataframe1.loc[dataframe1["company_size"] == "601-1.000", "company_size"] = 2
dataframe1.loc[dataframe1["company_size"] == "1.000-5.000", "company_size"] = 3
dataframe1.loc[dataframe1["company_size"] == "5.000-10.000", "company_size"] = 3
dataframe1.loc[dataframe1["company_size"] == "10.000 ve üzeri", "company_size"] = 4


dataframe1.loc[dataframe1["raise_period"] == "4 veya üzeri", "raise_period"] = 4


def convert_salary(salary):
    if isinstance(salary, str):
        # Extract only digits and '-' character
        salary = ''.join(re.findall(r'\d+|-', salary))
        if '-' in salary:
            salary_range = salary.split('-')
            return sum(map(int, salary_range)) / 2
        else:
            return int(salary)
    else:
        return 0

dataframe1['mean_salary'] = dataframe1['salary'].apply(convert_salary)


#currency transform using exchange rates turkish lira to dolar for mean salary, so if currency is 1 convert it to dolar
dataframe1.loc[dataframe1["currency"] == 1, "mean_salary"] = dataframe1["mean_salary"] / 32.2
dataframe1.loc[(dataframe1["currency"].str.contains("Euro")) & (dataframe1["mean_salary"] != 0), "mean_salary"] = dataframe1["mean_salary"] / 0.92
dataframe1.loc[(dataframe1["currency"].str.contains("Sterlin")) & (dataframe1["mean_salary"] != 0), "mean_salary"] = dataframe1["mean_salary"] / 0.79 

#mean salary is converted to int
dataframe1["mean_salary"] = dataframe1["mean_salary"].astype(int)

#remove currency and salary columns and their values
dataframe1.drop(['currency', 'salary'], axis=1, inplace=True)



#unique_positions = dataframe1['position'].unique()
#print(unique_positions)

title_mapping = {
  'Fullstack Developer / Engineer': 'Full Stack Development',
  'Full Stack Developer': 'Full Stack Development',
  'Software Engineer': 'Software Development',
  'Software Design Engineer': 'Software Development',
  'Backend Developer / Engineer': 'Backend Development',
  'Back-end Developer': 'Backend Development',
  'Frontend Developer / Engineer': 'Frontend Development',
  'Front-end Developer': 'Frontend Development',
  'Mobile Developer (Cross Platform)': 'Mobile Development',
  'Mobile Application Developer (iOS)': 'Mobile Development',
  'Mobile Application Developer (Android)': 'Mobile Development',
  'Mobile Application Developer (Full Stack)': 'Mobile Development',
  'Android Developer': 'Mobile Development',
  'iOS Developer': 'Mobile Development',
  'Game Developer / Engineer': 'Game Development',
  'Game Developer': 'Game Development',
  'Embedded Developer / Engineer': 'Embedded Systems',
  'Embedded Software Developer': 'Embedded Systems',
  'Integration Developer': 'Integration Development',
  'CRM Developer': 'Integration Development',
  'ERP Developer': 'Integration Development',
  'SAP Consultant': 'SAP/ABAP Development',
  'ABAP Consultant': 'SAP/ABAP Development',
  'SAP/ABAP Developer & Consultant': 'SAP/ABAP Development',
  'Solutions Architect': 'Architectural Roles',
  'Solution Architect': 'Architectural Roles',
  'Software Architect': 'Architectural Roles',
  'Enterprise Architect': 'Architectural Roles',
  'Cloud Architect': 'Architectural Roles',
  'Salesforce Architect': 'Architectural Roles',
  'Salesforce Developer': 'Salesforce Development',
  'Salesforce Consultant': 'Salesforce Development',
  'Solution Developer / Specialist': 'Specialist Development',
  'Data Warehouse Developer': 'Specialist Development',
  'Prompt Engineer': 'Specialist Development',
  'Data Scientist': 'Data Science',
  'Data Engineer': 'Data Engineering',
  'Data engineer': 'Data Engineering',
  'Data Analyst': 'Data Analysis',
  'Business Intelligence (BI) Developer / Engineer': 'Business Intelligence',
  'Data Storage Engineer': 'Data Storage and Management',
  'Database Administrator': 'Data Storage and Management',
  'Database Administrator (DBA)': 'Data Storage and Management',
  'SecOps Engineer': 'Operations Security',
  'Cyber Security Engineer': 'Cyber Security',
  'Cyber Security': 'Cyber Security',
  'Application Security Engineer': 'Application Security',
  'DevSecOps': 'DevSecOps',
  'DevOps': 'DevOps',
  'DevOps Engineer': 'DevOps',
  'Cloud Engineer': 'Cloud Engineering',
  'Cloud Platform Engineer': 'Cloud Engineering',
  'Backup Engineer': 'System Administration',
  'System Administrator': 'System Administration',
  'System Admin & Engineer': 'System Administration',
  'Site Reliability Engineer': 'System Administration',
  'System Support Engineer': 'System Administration',
  'Virtualization Specialist': 'System Administration',
  'Team Lead': 'Team and Technical Leadership',
  'Tech Lead': 'Team and Technical Leadership',
  'Team / Tech Lead': 'Team and Technical Leadership',
  'Network Engineer': 'Network Engineering',
  'Blockchain Developer / Engineer': 'Blockchain Development',
  'Product Manager': 'Product Management',
  'Business Development Specialist': 'Business Development',
  'IT Specialist': 'IT Support',
  '3D Artist': 'Creative Design',
  'Instructor': 'Education & Training',
  'Research Engineer': 'Research & Development',
  'Intern': 'Internship',
  'Agile Coach': 'Agile Methodology',
  'Machine Learning Engineer': 'Machine Learning',
  'Software Design Engineer': 'Software Development',  # Consider a subcategory if needed
  'RPA Developer': 'Integration Development',  # Consider a subcategory of Integration Development
  'Oracle Developer': 'Backend Development', # Consider a subcategory of Backend Development
}

dataframe1['position'] = dataframe1['position'].map(title_mapping)


#after the data preprocessing save the data as a new csv file
dataframe1.to_csv('final_data.csv', index=False)
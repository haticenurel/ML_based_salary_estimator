import pandas as pd

# Read the Excel file
df = pd.read_excel('Other2.xlsx')

# Convert to CSV without repeating the index
df.to_csv('Other2.csv', index=False)

df1 = pd.read_excel('outputOther1.xlsx')
df1.to_csv('Other1.csv', index=False)


tech_mapping = {
    'SQL': 'SQL',
    "Javascript / Typescript ve bağlı framework'ler": 'JavaScript / TypeScript and related frameworks',
    'JavaScript | Html | Css': 'JavaScript / TypeScript and related frameworks',
    'Jira / Asana / Trello / Bitrix24 ve benzeri PM araçları': 'Project Management Tools',
    'C# / .NET Framework': 'C# / .NET',
    '.Net': 'C# / .NET',
    "Java ve bağlı framework'ler": 'Java and related frameworks',
    'Java': 'Java and related frameworks',
    'ChatGPT': 'ChatGPT',
    'Cloud araçları ( AWS, Azure, GCP vs)': 'Cloud Tools (AWS, Azure, GCP etc.)',
    'Docker / containerd / Hyper-V / LXC / Podman': 'Docker / containerd / Hyper-V / LXC / Podman',
    'DevOps araçları': 'DevOps Tools',
    'Python': 'Python',
    'Linux': 'Linux',
    'Microsoft Office Araçları': 'Microsoft Office Tools',
    'Figma / XD ve diğer tasarım araçları': 'Design Tools (Figma / XD etc.)',
    'Kubernetes': 'Kubernetes',
    'NoSQL': 'NoSQL',
    'PHP': 'PHP',
    'Php': 'PHP',
    'C, C++': 'C, C++',
    'C / C++': 'C, C++',
    'Kotlin': 'Kotlin',
    'Swift': 'Swift',
    'Golang': 'Golang',
    'Go': 'Golang',
    'No-code / Low-code Araçları': 'No-code / Low-code Tools',
    'Flutter': 'Flutter',
    'SAP': 'SAP',
    'Adobe CC araçları': 'Adobe CC Tools',
    'JavaScript | Html | Css': 'JavaScript / TypeScript and related frameworks',
    'React': 'React',
    'NodeJS': 'NodeJS',
    'Angular': 'Angular',
    'Vue': 'Vue',
    'React Native': 'React Native',
    'Unity': 'Unity'
}

#rename the column names of datasets according to tech_mapping dictionary for the first data file
df1 = df1.rename(columns=tech_mapping)
df1.to_csv('rename1.csv', index=False)

#rename the column names of datasets according to tech_mapping dictionary for the second data file
df = df.rename(columns=tech_mapping)
df.to_csv('rename2.csv', index=False)


#just take tech mapping columns from rename1.csv and rename2.csv
df1 = pd.read_csv('rename1.csv')
df2 = pd.read_csv('rename2.csv')






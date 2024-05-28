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


common_columns = df.columns.intersection(df1.columns)
print(common_columns)

#combine common columns of two datasets into one dataset
combined_df = pd.concat([df[common_columns], df1[common_columns].fillna(0)])
combined_df.to_csv('combined.csv', index=False)

# #combine the two columns into one column and convert to a csv file like this SQL and SQL in one column names as SQL
# combined_df1 = pd.concat([df['Python'], df1['Python'].fillna(0)])
# combined_df1.to_csv('1.csv', index=False)

# combined_df2 = pd.concat([df['JavaScript / TypeScript and related frameworks'], df1['JavaScript / TypeScript and related frameworks'].fillna(0)])
# combined_df2.to_csv('2.csv', index=False)


# print(df.columns)
# print(df1.columns)

# combined_df3 = pd.concat([df['Project Management Tools'], df1['Project Management Tools'].fillna(0)])
# combined_df3.to_csv('3.csv', index=False)

# combined_df4 = pd.concat([df['C# / .NET'], df1['C# / .NET'].fillna(0)])
# combined_df4.to_csv('4.csv', index=False)

# combined_df5 = pd.concat([df['Java and related frameworks'], df1['Java and related frameworks'].fillna(0)])
# combined_df5.to_csv('5.csv', index=False)

# combined_df6 = pd.concat([df['ChatGPT'], df1['ChatGPT'].fillna(0)])
# combined_df6.to_csv('6.csv', index=False)

# combined_df7 = pd.concat([df['Cloud Tools (AWS, Azure, GCP etc.)'], df1['Cloud Tools (AWS, Azure, GCP etc.)'].fillna(0)])
# combined_df7.to_csv('7.csv', index=False)

# combined_df8 = pd.concat([df['Docker / containerd / Hyper-V / LXC / Podman'], df1['Docker / containerd / Hyper-V / LXC / Podman'].fillna(0)])
# combined_df8.to_csv('8.csv', index=False)

# combined_df9 = pd.concat([df['DevOps Tools'], df1['DevOps Tools'].fillna(0)])
# combined_df9.to_csv('9.csv', index=False)

# combined_df10 = pd.concat([df['Linux'], df1['Linux'].fillna(0)])
# combined_df10.to_csv('10.csv', index=False)

# combined_df11 = pd.concat([df['Microsoft Office Tools'], df1['Microsoft Office Tools'].fillna(0)])
# combined_df11.to_csv('11.csv', index=False)

# combined_df12 = pd.concat([df['Design Tools (Figma / XD etc.)'], df1['Design Tools (Figma / XD etc.)'].fillna(0)])
# combined_df12.to_csv('12.csv', index=False)

# combined_df13 = pd.concat([df['Kubernetes'], df1['Kubernetes'].fillna(0)])
# combined_df13.to_csv('13.csv', index=False)

# combined_df14 = pd.concat([df['NoSQL'], df1['NoSQL'].fillna(0)])
# combined_df14.to_csv('14.csv', index=False)

# combined_df15 = pd.concat([df['PHP'], df1['PHP'].fillna(0)])
# combined_df15.to_csv('15.csv', index=False)

# combined_df16 = pd.concat([df['C, C++'], df1['C, C++'].fillna(0)])
# combined_df16.to_csv('16.csv', index=False)

# combined_df17 = pd.concat([df['Kotlin'], df1['Kotlin'].fillna(0)])
# combined_df17.to_csv('17.csv', index=False)

# combined_df18 = pd.concat([df['Swift'], df1['Swift'].fillna(0)])
# combined_df18.to_csv('18.csv', index=False)

# combined_df19 = pd.concat([df['Golang'], df1['Golang'].fillna(0)])
# combined_df19.to_csv('19.csv', index=False)

# combined_df20 = pd.concat([df['No-code / Low-code Tools'], df1['No-code / Low-code Tools'].fillna(0)])
# combined_df20.to_csv('20.csv', index=False)

# combined_df21 = pd.concat([df['Flutter'], df1['Flutter'].fillna(0)])
# combined_df21.to_csv('21.csv', index=False)

# combined_df22 = pd.concat([df['SAP'], df1['SAP'].fillna(0)])
# combined_df22.to_csv('22.csv', index=False)

# combined_df23 = pd.concat([df['Adobe CC Tools'], df1['Adobe CC Tools'].fillna(0)])
# combined_df23.to_csv('23.csv', index=False)



# # concate these new csv files into one csv file as total data file
# df2 = pd.read_csv('1.csv')
# df3 = pd.read_csv('2.csv')
# df4 = pd.read_csv('3.csv')
# df5 = pd.read_csv('4.csv')
# df6 = pd.read_csv('5.csv')
# df7 = pd.read_csv('6.csv')
# df8 = pd.read_csv('7.csv')
# df9 = pd.read_csv('8.csv')
# df10 = pd.read_csv('9.csv')
# df11 = pd.read_csv('10.csv')
# df12 = pd.read_csv('11.csv')
# df13 = pd.read_csv('12.csv')
# df14 = pd.read_csv('13.csv')
# df15 = pd.read_csv('14.csv')
# df16 = pd.read_csv('15.csv')
# df17 = pd.read_csv('16.csv')
# df18 = pd.read_csv('17.csv')
# df19 = pd.read_csv('18.csv')
# df20 = pd.read_csv('19.csv')
# df21 = pd.read_csv('20.csv')
# df22 = pd.read_csv('21.csv')
# df23 = pd.read_csv('22.csv')
# df24 = pd.read_csv('23.csv')

# final_df = pd.concat([df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24], axis=1)
# final_df.to_csv('techdata.csv', index=False)







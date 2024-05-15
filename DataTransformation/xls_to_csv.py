#take these two data files and convert them to one csv file together

import pandas as pd

#read in the two data files
df1 = pd.read_excel('2024_Yazılım_Sektörü_Maaş.xlsx')
df2 = pd.read_excel('2024-yazilim-sektoru-maaslari.xlsx')

#just take these columns from the first data file "Cinsiyet, Şirketiniz hangi şehirde? (Eğer Türkiye ise),Çalışma şekliniz nedir?, Şirketinizin çalışan sayısı nedir? ,Hangi pozisyonda çalışıyorsunuz?, Çalıştığınız şirketteki unvanınız nedir?, Deneyim , Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz? , Kazancınız hangi para biriminde?, Senede kaç kez zam alıyorsunuz? ,Maaş / Aylık Türk Lirası cinsinden          (Ortalama "NET" ücret)
df1 = df1[['Cinsiyet', 'Şirketiniz hangi şehirde? (Eğer Türkiye ise)', 'Çalışma şekliniz nedir?', 'Şirketinizin çalışan sayısı nedir?', 'Hangi pozisyonda çalışıyorsunuz?', 'Çalıştığınız şirketteki unvanınız nedir?', 'Deneyim', 'Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz?', 'Kazancınız hangi para biriminde?', 'Senede kaç kez zam alıyorsunuz?', 'Maaş / Aylık Türk Lirası cinsinden          (Ortalama "NET" ücret)']]
#convert to these taken columns to a csv file 
df1.to_csv('2024_Yazılım_Sektörü_Maaş.csv', index=False)

# just take these columns from the second data gender, city, work_type, company_size, position, level, experience, tech_stack, currency, raise_period, salary
df2 = df2[['gender', 'city', 'work_type', 'company_size', 'position', 'level', 'experience', 'tech_stack', 'currency', 'raise_period', 'salary']]
#convert to these taken columns to a csv file
df2.to_csv('2024-yazilim-sektoru-maaslari.csv', index=False)

# take as one column from the first data file and the second data file 
df1 = pd.read_csv('2024_Yazılım_Sektörü_Maaş.csv')
df2 = pd.read_csv('2024-yazilim-sektoru-maaslari.csv')
# her iki sütunu birleştir tek bir sütun haline getir tek tek 

#combine the two columns into one column and convert to a csv file like this Cinsiyet and gender in one column names as Gender
combined_df = pd.concat([df1['Cinsiyet'], df2['gender']])
combined_df.to_csv('new.csv', index=False)

#combine the two columns into one column as second column and convert to a csv file like this Şirketiniz hangi şehirde? (Eğer Türkiye ise) and city in one column names as City

combined_df2 = pd.concat([df1['Şirketiniz hangi şehirde? (Eğer Türkiye ise)'], df2['city']])

combined_df2.to_csv('new2.csv', index=False)

#combine the two columns into one column as third column and convert to a csv file like this Çalışma şekliniz nedir? and work_type in one column names as Work_type, Şirketinizin çalışan sayısı nedir? and company_size in one column names as Company_size, Hangi pozisyonda çalışıyorsunuz? and position in one column names as Position, Çalıştığınız şirketteki unvanınız nedir? and level in one column names as Level, Deneyim and experience in one column names as Experience, Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz? and tech_stack in one column names as Tech_stack, Kazancınız hangi para biriminde? and currency in one column names as Currency, Senede kaç kez zam alıyorsunuz? and raise_period in one column names as Raise_period, Maaş / Aylık Türk Lirası cinsinden (Ortalama "NET" ücret) and salary in one column names as Salary

combined_df3 = pd.concat([df1['Çalışma şekliniz nedir?'], df2['work_type']])
combined_df4 = pd.concat([df1['Şirketinizin çalışan sayısı nedir?'], df2['company_size']])
combined_df5 = pd.concat([df1['Hangi pozisyonda çalışıyorsunuz?'], df2['position']])
combined_df6 = pd.concat([df1['Çalıştığınız şirketteki unvanınız nedir?'], df2['level']])
combined_df7 = pd.concat([df1['Deneyim'], df2['experience']])
combined_df9 = pd.concat([df1['Kazancınız hangi para biriminde?'], df2['currency']])
combined_df10 = pd.concat([df1['Senede kaç kez zam alıyorsunuz?'], df2['raise_period']])
combined_df11 = pd.concat([df1['Maaş / Aylık Türk Lirası cinsinden          (Ortalama "NET" ücret)'], df2['salary']])
combined_df3.to_csv('new3.csv', index=False)
combined_df4.to_csv('new4.csv', index=False)
combined_df5.to_csv('new5.csv', index=False)
combined_df6.to_csv('new6.csv', index=False)
combined_df7.to_csv('new7.csv', index=False)
combined_df9.to_csv('new9.csv', index=False)
combined_df10.to_csv('new10.csv', index=False)
combined_df11.to_csv('new11.csv', index=False)

# concate these new csv files into one csv file as total data file 
df3 = pd.read_csv('new.csv')
df4 = pd.read_csv('new2.csv')
df5 = pd.read_csv('new3.csv')
df6 = pd.read_csv('new4.csv')
df7 = pd.read_csv('new5.csv')
df8 = pd.read_csv('new6.csv')
df9 = pd.read_csv('new7.csv')
df11 = pd.read_csv('new9.csv')
df12 = pd.read_csv('new10.csv')
df13 = pd.read_csv('new11.csv')

# collect all the data files into one csv file it will be the final data file and it should contain all the columns from the first and second data files
final_df = pd.concat([df3, df4, df5, df6, df7, df8, df9, df11, df12, df13], axis=1)
final_df.to_csv('final.csv', index=False)


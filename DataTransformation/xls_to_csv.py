import pandas as pd
 
dataframe1 = pd.read_excel('2024-yazilim-sektoru-maaslari.xlsx')

dataframe1.loc[dataframe1["gender"] == "Erkek", "gender"] = 1
dataframe1.loc[dataframe1["gender"] == "Kadın", "gender"] = 0

dataframe1.loc[dataframe1["currency"] != "₺ - Türk Lirası", "currency"] = 0
dataframe1.loc[dataframe1["currency"] == "₺ - Türk Lirası", "currency"] = 1

dataframe1.loc[dataframe1["level"] == "Junior", "level"] = 1
dataframe1.loc[dataframe1["level"] == "Middle", "level"] = 2
dataframe1.loc[dataframe1["level"] == "Senior", "level"] = 3

dataframe1.loc[dataframe1["experience"] == "0 - 1 Yıl", "experience"] = 1
dataframe1.loc[dataframe1["experience"] == "1 - 3 Yıl", "experience"] = 2
dataframe1.loc[dataframe1["experience"] == "3 - 5 Yıl", "experience"] = 3
dataframe1.loc[dataframe1["experience"] == "5 - 7 Yıl", "experience"] = 4
dataframe1.loc[dataframe1["experience"] == "7 - 10 Yıl", "experience"] = 5
dataframe1.loc[dataframe1["experience"] == "10 - 12 Yıl", "experience"] = 6
dataframe1.loc[dataframe1["experience"] == "12 - 14 Yıl", "experience"] = 7
dataframe1.loc[dataframe1["experience"] == "15 Yıl ve üzeri", "experience"] = 8


company_size_mapping = {"1 - 5 Kişi": 1, "6 - 10 Kişi": 2, "11 - 20 Kişi": 3,"21 - 50 Kişi": 4,"51 - 100 Kişi": 5,"101 - 249 Kişi": 6,"250+": 7}

dataframe1["company_size"] = dataframe1["company_size"].map(company_size_mapping)


# first we want to detect different countries
dataframe1.loc[dataframe1['city'].str.contains(r'^\* ', na=False), 'city'] = 3
# Second we want to detect which ones are not istanbul
dataframe1.loc[(dataframe1["city"] != "İstanbul") & (dataframe1["city"] != 3), "city"] = 1
# then find and assign 1 to istanbuls
dataframe1.loc[dataframe1["city"] == "İstanbul", "city"] = 2

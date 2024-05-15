import pandas as pd

#read final.csv data
dataframe1 = pd.read_csv('final.csv')

dataframe1.loc[dataframe1["gender"] == "Erkek", "gender"] = 1
dataframe1.loc[dataframe1["gender"] == "Kadın", "gender"] = 0
dataframe1.loc[dataframe1["gender"] == "Belirtmek İstemiyorum", "gender"] = 2

dataframe1.loc[dataframe1["city"] == "İstanbul", "city"] = 1
dataframe1.loc[dataframe1["city"] == "34 İstanbul", "city"] = 1
#istanbul ve 34 istanbul aynı şehir olduğu için 1 olarak işaretlendi bunların dışındaki şehirler 0 olarak işaretlendi
dataframe1.loc[dataframe1["city"] != 1, "city"] = 0


dataframe1.loc[dataframe1["currency"] != "₺ - Türk Lirası", "currency"] = 0
dataframe1.loc[dataframe1["currency"] == "₺ - Türk Lirası", "currency"] = 1

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


#after the data preprocessing save the data as a new csv file
dataframe1.to_csv('final_data.csv', index=False)

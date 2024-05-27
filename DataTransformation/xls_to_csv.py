import pandas as pd
import xlsxwriter
from pathlib import Path
path=Path("2024-yazilim-sektoru-maaslari.xlsx")
# path=Path("2024_Yazılım_Sektörü_Maaş.xlsx")

dataframe1 = pd.read_excel(path)
dataframe1 = pd.read_excel(path)

dataframe1.loc[dataframe1["gender"] == "Erkek", "gender"] = 1
dataframe1.loc[dataframe1["gender"] == "Kadın", "gender"] = 0
dataframe1.loc[dataframe1["gender"] == "Belirtmek İstemiyorum", "gender"] = 2

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

dataframe1.loc[dataframe1["company"] != "Kurumsal", "company"] = 0
dataframe1.loc[dataframe1["company"] == "Kurumsal", "company"] = 1




# # messss DATA 2024_Yazılım_Sektörü_Maaş.xlsx -----------------------------------------------------------------------
# # tech mapping starts ---------------
# techs = []
# tech_stack_mapping = {}
# def addToList(tech_stack):
#     global techs
#     try:
#         tech_list = tech_stack.split('\n')
#         techs.extend(tech_list)
#     except AttributeError:
#         return ()
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         return ()
    
# dataframe1['Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz?'].apply(addToList)
# counter = 0

# # tech mapping ends -----------

# for tech in techs:
#     tech_stack_mapping[tech] = techs.count(tech)
# # print(tech_stack_mapping)
# techSearchList=[]
# for i in sorted(tech_stack_mapping.items() ,reverse=True, key=lambda x:x[1])[:24]:
#     techSearchList.append(i[0])
#     print(i[1])



# for techDF in techSearchList:
#     dataframe1.loc[dataframe1["Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz?"].str.contains(r''+techDF+'', na=False), techDF] = int(1)
#     dataframe1.loc[dataframe1["Ağırlıklı olarak hangi teknolojileri / dilleri kullanıyorsunuz?"].str.contains(r''+techDF+'', na=False) == False, techDF] = int(0)

# # messss ends -------------------------------------------------------------------

# messss DATA 2024-yazilim-sektoru-maaslari.xlsx -----------------------------------------------------------------------
# tech mapping starts ---------------
techs = []
tech_stack_mapping = {}
def addToList(tech_stack):
    global techs
    try:
        tech_list = tech_stack.split(';')
        techs.extend(tech_list)
    except AttributeError:
        return ()
    except Exception as e:
        print(f"Error occurred: {e}")
        return ()
    
dataframe1['tech_stack_tuple'] = dataframe1['tech_stack'].apply(addToList)
counter = 0

# tech mapping ends -----------

for tech in techs:
    tech_stack_mapping[tech] = techs.count(tech)
# print(tech_stack_mapping)
techSearchList=[]
for i in sorted(tech_stack_mapping.items() ,reverse=True, key=lambda x:x[1])[:16]:
    techSearchList.append(i[0])
    print(i[1])



for techDF in techSearchList:
    dataframe1.loc[dataframe1["tech_stack"].str.contains(r''+techDF+'', na=False), techDF] = int(1)
    dataframe1.loc[dataframe1["tech_stack"].str.contains(r''+techDF+'', na=False) == False, techDF] = int(0)

# messss ends -------------------------------------------------------------------

# dataframe1["Office"] = dataframe1["work_type"].apply(lambda work_type: 1 if work_type == "Ofis" or work_type == "Ofiste" else 0)
# dataframe1["Hybrid"] = dataframe1["work_type"].apply(lambda work_type: 1 if work_type == "Hibrit" or work_type == "Hybrid" or work_type == "Hibrit (Ofis + Remote)" or work_type == "Şu an hibrit ama ofise döneceğiz." else 0)
# dataframe1["Remote"] = dataframe1["work_type"].apply(lambda work_type: 1 if work_type == "Şu an remote ama hibrite döneceğiz." or work_type == "Remote" else 0)
# dataframe1.drop(['work_type'], axis=1,inplace=True)

# to new file
file_path = 'outputOther1.xlsx'
dataframe1.to_excel(file_path, index=False)




















# -------------------------------------------
# techs = []

# def addToList(tech_stack):
#     global techs
#     try:
#         if 
#     except AttributeError:
#         return ()
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         return ()
    
# dataframe1['Hangi pozisyonda çalışıyorsunuz?'].apply(addToList)

# print(techs)
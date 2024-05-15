import pandas as pd
df = pd.read_excel(r'C:\Users\merve\OneDrive\Belgeler\GitHub\ML_based_salary_estimator\DataTransformation\2024_Yazılım_Sektörü_Maaş.xlsx')
df = df.drop('Submission Date', axis=1)
df.to_excel('2024_I_-_Yazılım_Sektörü_Maaş_A2024-02-05_15_59_12.xlsx', index=False) 

# Display the contents
print(df)
# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('last_final_data_with_id.csv')
data.dropna(how="any", inplace=True)

X = data.drop(columns=['mean_salary'])
Y = data['mean_salary']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)
corr = data[["experience","mean_salary"]].corr()

print(corr)

sns.heatmap(corr,annot=True)
plt.show()

data['position'].value_counts().plot(kind="bar")
plt.show()

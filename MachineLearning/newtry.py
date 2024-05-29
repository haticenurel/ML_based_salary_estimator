# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('./data/last_final_data.csv')
data.dropna(how="any", inplace=True)

X = data.drop(columns=['mean_salary'])
Y = data['mean_salary']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)
corr = data[["experience","mean_salary"]].corr()

print(corr)

# sns.heatmap(corr,annot=True)
# plt.show()

# data['position'].value_counts().plot(kind="bar")
# plt.show()

# data['JavaScript / TypeScript and related frameworks'].value_counts().plot(kind="barh")
# plt.xlabel("Frequency")  # Set x-axis label
# plt.ylabel("Category")
# plt.show()

category_counts = data['JavaScript / TypeScript and related frameworks'].value_counts().to_dict()
category_labels = {key: f"{key} ({value})" for key, value in category_counts.items()}  # Add frequency in brackets

# Option 2: Using list comprehension (simpler)
category_labels = [f"{'has' if name == 1 else 'has not'} ({count})" for name, count in data['JavaScript / TypeScript and related frameworks'].value_counts().items()]

data['JavaScript / TypeScript and related frameworks'].value_counts().plot(kind="barh")
plt.yticks(range(len(category_labels)), category_labels)  # Set custom y-axis labels with positions
plt.show()
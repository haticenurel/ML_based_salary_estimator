# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
# Read the data (replace 'your_data.csv' with the actual file path)
data = pd.read_csv('./data/last_final_data.csv')
data.dropna(how="any", inplace=True)

Label_Encoder = LabelEncoder()
data["position"] = Label_Encoder.fit_transform(data["position"])
data["office"] = Label_Encoder.fit_transform(data["office"])
data["hybrid"] = Label_Encoder.fit_transform(data["hybrid"])
data["remote"] = Label_Encoder.fit_transform(data["remote"])
# Separate features (X) and target (Y)
X = data.drop(columns=['mean_salary'])
Y = data['mean_salary']
# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)
# corr = data[["experience","mean_salary"]].corr()


Linear_regression_model = LinearRegression()

Linear_regression_model.fit(X_train,Y_train)

y_pred_lr = Linear_regression_model.predict(X_test)

df = pd.DataFrame({"y_Actual":Y_test,"y_Predicted":y_pred_lr})
df["Error"]= df["y_Actual"]-df["y_Predicted"]
df["abs_error"]= abs(df["Error"])
Mean_absolute_Error = df["abs_error"].mean()
print(Mean_absolute_Error)

print(X_test.shape)
print(y_pred_lr.shape)


plt.figure(figsize=(8, 6))
plt.scatter(Y_test, y_pred_lr, color='b', alpha=0.5)
plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color='r', linestyle='--')
plt.xlabel("Actual Values (y_Actual)")
plt.ylabel("Predicted Values (y_Predicted)")
plt.title("Actual vs. Predicted Values (Linear Regression)")
plt.grid(True)
plt.show()
#train and test the data using regression model
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder

# Load the data
data = pd.read_csv('../DataTransformation/last_final_data.csv')


# Instantiate the encoder
le = LabelEncoder()

# Iterate over all the values of each column and extract their dtypes
for col in data.columns:
    # Compare if the dtype is object
    if data[col].dtype=='object':
    # Use LabelEncoder to do the numeric transformation
        data[col]=le.fit_transform(data[col])

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

# Split the dataset into 80% training and 20% testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Use the Linear Regression model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Get the predictions
Y_pred = regressor.predict(X_test)

# Get the R-Squared
r2 = r2_score(Y_test, Y_pred)

# Get the Mean Squared Error
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error: ", mse)

# Get the Mean Absolute Error
mae = mean_absolute_error(Y_test, Y_pred)
print("Mean Absolute Error: ", mae)


# Ensure the directory exists
if not os.path.exists('MachineLearning'):
    os.makedirs('MachineLearning')

# Save the model

joblib.dump(regressor, 'MachineLearning/model.pkl')
print("Model has been saved as model.pkl")

# Save the data columns
model_columns = list(data.columns)
joblib.dump(model_columns, 'MachineLearning/model_columns.pkl')
print("Model columns have been saved as model_columns.pkl")

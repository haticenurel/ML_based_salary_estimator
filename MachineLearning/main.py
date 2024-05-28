import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the data
data = pd.read_csv('../DataTransformation/last_final_data.csv')

# Preprocessing
# Check for missing values
print(data.isnull().sum())

# Encode categorical variables
categorical_features = ['city', 'company_size', 'position', 'level', 'office', 'hybrid', 'remote']
numerical_features = ['experience', 'raise_period', 'JavaScript / TypeScript and related frameworks',
                      'C# / .NET', 'Java and related frameworks', 'Python', 'PHP', 'C, C++', 
                      'Kotlin', 'Swift', 'Golang', 'Flutter']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Split the data into features and target
X = data.drop('mean_salary', axis=1)
y = data['mean_salary']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print('MAE:', mean_absolute_error(y_test, y_pred))
print('MSE:', mean_squared_error(y_test, y_pred))
print('R2:', r2_score(y_test, y_pred))


# Save the model
import joblib
joblib.dump(model, 'model.pkl')

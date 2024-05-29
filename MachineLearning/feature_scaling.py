import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the data
data = pd.read_csv('../DataTransformation/last_final_data.csv')

# Define features and target
X = data.drop('mean_salary', axis=1)
y = data['mean_salary']

# Categorical and numerical features
categorical_features = ['city', 'company_size', 'position', 'level', 'office', 'hybrid', 'remote']
numerical_features = ['experience', 'raise_period', 'JavaScript / TypeScript and related frameworks',
                      'C# / .NET', 'Java and related frameworks', 'Python', 'PHP', 'C, C++', 
                      'Kotlin', 'Swift', 'Golang', 'Flutter']

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])


from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(random_state=42)
}

# Train and evaluate models
for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f'{name} - MAE: {mean_absolute_error(y_test, y_pred)}, MSE: {mean_squared_error(y_test, y_pred)}, R2: {r2_score(y_test, y_pred)}')

# Choose the best model (for example, Random Forest)
best_model = Pipeline(steps=[('preprocessor', preprocessor), ('model', RandomForestRegressor(random_state=42))])
best_model.fit(X_train, y_train)






import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset california_housing
housing = fetch_california_housing()

# Create a DataFrame from the dataset
data = pd.DataFrame(housing.data, columns=housing.feature_names)
data['PRICE'] = housing.target

# Display the first few rows of the dataset
print(data.head())

# Features (independent variables)
X = data.drop('PRICE', axis=1)

# Labels (dependent variable)
y = data['PRICE']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Display the coefficients of the model
print(f"Coefficients: {model.coef_}")

# Save the model to a file using csv format
np.savetxt("./models/model.csv", model.coef_, delimiter=",")

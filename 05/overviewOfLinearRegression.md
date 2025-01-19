Let's go through the steps to implement and evaluate simple linear and logistic regression models using Scikit-Learn, a popular machine learning library in Python.

### Simple Linear Regression

Linear regression is a statistical method to model the relationship between a dependent variable and one or more independent variables. In simple linear regression, we have one independent variable.

#### Steps to Implement Linear Regression:

1. **Import Libraries**: Import necessary libraries such as NumPy, Pandas, and Scikit-Learn.
2. **Load Dataset**: Load the dataset you want to use.
3. **Preprocess Data**: Handle missing values, encode categorical variables, and split the data into training and testing sets.
4. **Train Model**: Use Scikit-Learn's `LinearRegression` to train the model.
5. **Evaluate Model**: Evaluate the model's performance using metrics like Mean Squared Error (MSE) and R² score.

#### Example Code:

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
# For example, using a hypothetical dataset 'data.csv'
data = pd.read_csv('data.csv')

# Assume 'X' is the feature and 'y' is the target variable
X = data[['feature_column']]
y = data['target_column']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
```

### Simple Logistic Regression

Logistic regression is used for binary classification problems. It models the probability that a given input belongs to a particular class.

#### Steps to Implement Logistic Regression:

1. **Import Libraries**: Import necessary libraries such as NumPy, Pandas, and Scikit-Learn.
2. **Load Dataset**: Load the dataset you want to use.
3. **Preprocess Data**: Handle missing values, encode categorical variables, and split the data into training and testing sets.
4. **Train Model**: Use Scikit-Learn's `LogisticRegression` to train the model.
5. **Evaluate Model**: Evaluate the model's performance using metrics like accuracy, precision, recall, and F1 score.

#### Example Code:

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
# For example, using a hypothetical dataset 'data.csv'
data = pd.read_csv('data.csv')

# Assume 'X' is the feature and 'y' is the target variable
X = data[['feature_column']]
y = data['target_column']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
```

### Summary

- **Linear Regression**: Used for predicting a continuous target variable. Evaluated using MSE and R² score.
- **Logistic Regression**: Used for binary classification problems. Evaluated using accuracy, precision, recall, and F1 score.

These examples provide a basic introduction to implementing and evaluating linear and logistic regression models using Scikit-Learn. You can further enhance these models by performing feature engineering, hyperparameter tuning, and using more advanced evaluation metrics.
Let's dive into a detailed explanation of Linear Regression and Logistic Regression, including their concepts, mathematical foundations, and practical examples.

### Linear Regression

#### Concept

Linear regression is a statistical method used to model the relationship between a dependent variable (target) and one or more independent variables (features). The goal is to find the best-fitting straight line (or hyperplane in higher dimensions) that predicts the target variable based on the features.

#### Mathematical Foundation

The equation of a simple linear regression model (with one feature) is:

\[ y = \beta_0 + \beta_1 x + \epsilon \]

- \( y \): Dependent variable (target)
- \( x \): Independent variable (feature)
- \( \beta_0 \): Intercept (the value of \( y \) when \( x \) is 0)
- \( \beta_1 \): Slope (the change in \( y \) for a one-unit change in \( x \))
- \( \epsilon \): Error term (the difference between the actual and predicted values)

The goal is to find the values of \( \beta_0 \) and \( \beta_1 \) that minimize the sum of squared errors (SSE) between the actual and predicted values.

#### Example

Let's consider a dataset where we want to predict a person's salary based on their years of experience.

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
}
df = pd.DataFrame(data)

# Define the feature and target variable
X = df[['YearsExperience']]
y = df['Salary']

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

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression: Salary vs. Years of Experience')
plt.show()
```

### Logistic Regression

#### Concept

Logistic regression is a statistical method used for binary classification problems. It models the probability that a given input belongs to a particular class. Unlike linear regression, the output of logistic regression is a probability value between 0 and 1.

#### Mathematical Foundation

The equation of a logistic regression model is:

\[ P(y=1|x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}} \]

- \( P(y=1|x) \): Probability that the target variable \( y \) is 1 given the feature \( x \)
- \( \beta_0 \): Intercept
- \( \beta_1 \): Coefficient for the feature \( x \)
- \( e \): Base of the natural logarithm

The logistic function (sigmoid function) maps any real-valued number into the range [0, 1].

#### Example

Let's consider a dataset where we want to predict whether a student will pass (1) or fail (0) an exam based on their study hours.

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Define the feature and target variable
X = df[['StudyHours']]
y = df['Pass']

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

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict_proba(X)[:, 1], color='red')
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Probability of Passing vs. Study Hours')
plt.show()
```

### Summary

- **Linear Regression**: Used for predicting a continuous target variable. The relationship between the target and the feature(s) is modeled as a straight line. Evaluated using metrics like Mean Squared Error (MSE) and R² score.
- **Logistic Regression**: Used for binary classification problems. The relationship between the target and the feature(s) is modeled using the logistic function, which outputs probabilities. Evaluated using metrics like accuracy, precision, recall, and F1 score.

These examples provide a comprehensive introduction to implementing and evaluating linear and logistic regression models using Scikit-Learn. You can further enhance these models by performing feature engineering, hyperparameter tuning, and using more advanced evaluation metrics.

### Examples

Let's go through some simple examples of Linear Regression and Logistic Regression using Python and the Scikit-Learn library.

### Linear Regression Example

Let's consider a simple example where we want to predict a person's salary based on their years of experience.

#### Steps:
1. Import necessary libraries.
2. Create a sample dataset.
3. Split the dataset into training and testing sets.
4. Train a Linear Regression model.
5. Make predictions and evaluate the model.
6. Visualize the results.

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
}
df = pd.DataFrame(data)

# Define the feature and target variable
X = df[['YearsExperience']]
y = df['Salary']

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

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression: Salary vs. Years of Experience')
plt.show()
```

### Logistic Regression Example

Let's consider a simple example where we want to predict whether a student will pass (1) or fail (0) an exam based on their study hours.

#### Steps:
1. Import necessary libraries.
2. Create a sample dataset.
3. Split the dataset into training and testing sets.
4. Train a Logistic Regression model.
5. Make predictions and evaluate the model.
6. Visualize the results.

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Define the feature and target variable
X = df[['StudyHours']]
y = df['Pass']

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

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict_proba(X)[:, 1], color='red')
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Probability of Passing vs. Study Hours')
plt.show()
```

### Summary

- **Linear Regression**: Used for predicting a continuous target variable. The relationship between the target and the feature(s) is modeled as a straight line. Evaluated using metrics like Mean Squared Error (MSE) and R² score.
- **Logistic Regression**: Used for binary classification problems. The relationship between the target and the feature(s) is modeled using the logistic function, which outputs probabilities. Evaluated using metrics like accuracy, precision, recall, and F1 score.

These examples provide a basic introduction to implementing and evaluating linear and logistic regression models using Scikit-Learn. You can further enhance these models by performing feature engineering, hyperparameter tuning, and using more advanced evaluation metrics.
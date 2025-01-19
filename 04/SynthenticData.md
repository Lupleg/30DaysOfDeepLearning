Let's create a simple synthetic dataset that mimics the structure of the Boston Housing dataset. We'll generate random data for features and a target variable.

### Step-by-Step Guide to Create a Simple Dataset

#### Step 1: Import Required Libraries

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
```

#### Step 2: Create a Synthetic Dataset

We'll create a dataset with 5 features and 100 samples. The target variable will be a linear combination of the features with some added noise.

```python
# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100

# Generate random data for 5 features
X = np.random.rand(n_samples, 5)

# Generate random coefficients for a linear relationship
coefficients = np.array([3.5, -2.1, 4.0, 1.2, -3.3])

# Generate the target variable with some noise
y = X @ coefficients + np.random.randn(n_samples) * 0.5

# Create a DataFrame
feature_names = ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5']
data = pd.DataFrame(X, columns=feature_names)
data['PRICE'] = y

# Display the first few rows of the dataset
print(data.head())
```

#### Step 3: Prepare the Data

We'll split the data into features (X) and labels (y), and then into training and test sets.

```python
# Features (independent variables)
X = data.drop('PRICE', axis=1)

# Labels (dependent variable)
y = data['PRICE']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Step 4: Train the Model

We'll use a simple linear regression model for this example.

```python
# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
```

#### Step 5: Make Predictions

We'll use the trained model to make predictions on the test set.

```python
# Make predictions on the test set
y_pred = model.predict(X_test)
```

#### Step 6: Evaluate the Model

We'll evaluate the model's performance using Mean Squared Error (MSE).

```python
# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

#### Full Code

Here's the full code for the example with the synthetic dataset:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100

# Generate random data for 5 features
X = np.random.rand(n_samples, 5)

# Generate random coefficients for a linear relationship
coefficients = np.array([3.5, -2.1, 4.0, 1.2, -3.3])

# Generate the target variable with some noise
y = X @ coefficients + np.random.randn(n_samples) * 0.5

# Create a DataFrame
feature_names = ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5']
data = pd.DataFrame(X, columns=feature_names)
data['PRICE'] = y

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
```

### Explanation

1. **Creating the Synthetic Dataset**: We generate random data for 5 features and create a target variable as a linear combination of these features with some added noise.

2. **Preparing the Data**: We separate the features (X) from the labels (y) and split the data into training and test sets.

3. **Training the Model**: We initialize a linear regression model and train it using the training data.

4. **Making Predictions**: We use the trained model to make predictions on the test set.

5. **Evaluating the Model**: We calculate the Mean Squared Error (MSE) to evaluate the model's performance.

This example provides a basic introduction to machine learning and how to implement a simple linear regression model using Python and a synthetic dataset.

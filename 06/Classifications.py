import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target labels: 0 (setosa), 1 (versicolor), 2 (virginica)

# Step 3: Split the data into training and testing sets
# 80% of the data will be used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 5: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model's performance

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Generate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Generate classification report
class_report = classification_report(y_test, y_pred, target_names=iris.target_names)
print('Classification Report:')
print(class_report)

# Generate classification report as a dictionary
class_report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
print('Classification Report:')
print(class_report)

# Save the report to csv file
report = pd.DataFrame(class_report).transpose()
report.to_csv('./reports/classification_report.csv', index=False)
print('Classification Report saved to classification_report.csv')
Sure! Here are some examples using a few of the libraries mentioned. These examples will cover data manipulation with Pandas, data visualization with Matplotlib and Seaborn, and a simple machine learning model with Scikit-learn.

### Example 1: Data Manipulation with Pandas

```python
import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic operations
print("\nBasic Statistics:")
print(df.describe())

print("\nFilter rows where Age > 25:")
print(df[df['Age'] > 25])

print("\nAdd a new column:")
df['Age in 5 Years'] = df['Age'] + 5
print(df)
```

### Example 2: Data Visualization with Matplotlib and Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
tips = sns.load_dataset('tips')

# Matplotlib example: Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(tips['total_bill'], tips['tip'])
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Seaborn example: Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Total Bill Distribution by Day')
plt.show()
```

### Example 3: Simple Machine Learning Model with Scikit-learn

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
```

### Example 4: Natural Language Processing with NLTK

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural language processing (NLP) is a field of artificial intelligence."

# Tokenize the text
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)
```

### Example 5: Deep Learning with TensorFlow and Keras

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate dummy data
import numpy as np
X_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
X_test = np.random.random((200, 20))
y_test = np.random.randint(2, size=(200, 1))

# Build a simple neural network model
model = Sequential([
    Dense(64, activation='relu', input_dim=20),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
```

Feel free to run these examples in your Python environment to see how these libraries work!

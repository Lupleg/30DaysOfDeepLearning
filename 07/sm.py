from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import pandas as pd


# Creating a sample dataset
data = {
    'age': [25, 45, 35, 50, 23, 40, 30, 28, 33, 38],
    'salary': [50000, 100000, 75000, 120000, 45000, 80000, 60000, 52000, 70000, 85000],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}


df = pd.DataFrame(data)
print("Original Dataset:\n", df)
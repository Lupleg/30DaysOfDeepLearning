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

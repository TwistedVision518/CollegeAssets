import numpy as np
import pandas as pd

# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])

print(df)


# Create a Series
series = pd.Series([1, 2, 3, 4, 5])

print(series)


# Create a DataFrame from a dictionary
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

print(df)


# Create a DataFrame from a CSV file
df = pd.read_csv('data.csv')

print(df)


# Create a DataFrame from a JSON file
df = pd.read_json('data.json')

print(df)


# Create a DataFrame from a SQL query
df = pd.read_sql('SELECT * FROM data', con)

print(df)


# Create a DataFrame from a list of dictionaries
data = [{'A': 1, 'B': 4, 'C': 7}, {'A': 2, 'B': 5, 'C': 8}, {'A': 3, 'B': 6, 'C': 9}]
df = pd.DataFrame(data)

print(df)

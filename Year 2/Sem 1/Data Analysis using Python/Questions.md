QUESTION

Create one data frame with dimension 3,2 and column name should be PRN and final marks.

ANSWER

```python
import pandas as pd

# Create a DataFrame with 3 rows and 2 columns
data = {'PRN': [12345, 54321, 67890], 'Final Marks': [85, 92, 78]}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
```


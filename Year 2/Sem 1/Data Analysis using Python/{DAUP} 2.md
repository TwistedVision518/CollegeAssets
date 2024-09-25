In real world, we need labelled data. The labelled data need to be processed. In python we have *an important library known as pandas* which is helpful for processing labelled data.

The most useful data structure for data analysis is **data frame**.

**DDD** --> Data structures, Data analysis and Data frames

Data frames --> is analogous to *table* in RDBMS. Its structure is the same as tables. It is a collection of rows and columns.

### Basics of Data frames

The *pandas* library is especially used for handling data of different dimensions.

---
*Series* is one dimensional data and *data frame* is two dimensional labelled data holding any data type.

```python
prizelist = [100, 200, 300, 400]

productseries = pd.Series(prizelist, index=['Pen', 'Pencil', 'Book', 'Notebook'])

print(productseries)

OUTPUT:-
Pen         100
Pencil      200
Book        300
Notebook    400
dtype: int64
```

---

**Data frame** is the *most commonly used pandas object* and is represented as a *two dimensional labelled data structure* with columns of different types. It can be thought as a *table in RDBMS, or a spreadsheet in excel*.

A data frame is *created* using the `Dataframe()`

```python
Dataframe(data, columns=list_of_column_name)

data = represents multidimensional data
columns = list representing names of columns
```

```python
dataframe = pd.DataFrame(
    [
        [100, 200, 300, 400],
        [2, 3, 4, 5]
    ],
    columns=['Pen', 'Pencil', 'Book', 'Notebook']
)

print(dataframe)

OUTPUT:-
   Pen  Pencil  Book  Notebook
0  100     200   300       400
1    2       3     4         5
```

**Q:** Create one data frame with dimension $(3, 2)$ and column name should be `PRN` and `Final Marks`.

```python
dataframe = pd.DataFrame(
    [
        [1, 199],
        [2, 10],
        [3, 105],
        [4, 40],
    ],
    columns=['PRN', 'Final Marks']
)

OUTPUT:-
   PRN  Final Marks
0    1          199
1    2           10
2    3          105
3    4           40
```

#### Adding rows and columns to the data frame
We can add rows to an existing data frame from a new data frame using the `append()`.

We can also add a new column to the data frame, by writing the column name in `[]` along with the name of the data frame and assigning a list of items to it.

```python
import pandas as pd

productdf = pd.DataFrame([
    [100, 200, 300, 400],
    [1, 2, 3, 4]
],
    columns=['Pencil', 'Box', 'Book', 'Notebook']
)

print("The output is:\n", productdf)

productdf2 = pd.DataFrame([
    [15, 16, 17, 18],
    [21, 22, 23, 24]
],
    columns=['Pencil', 'Box', 'Book', 'Notebook']
)

print("The output is:\n", productdf2)

productdf3 = productdf._append(productdf2)

print("After adding rows, the final output is:\n", productdf3)

productdf3["Mobile"] = [1000, 200, 3000, 4000]
productdf3["Laptop"] = [10000, 2000, 30000, 40000]

print("After adding columns, The final output is:\n", productdf3)

```

**Q:** Consider the e-commerce system and perform the following things:
1. Create two data frame (select the column name as per your choice).
2. perform row and column addition and create the additional data frames.

```python
import pandas as pd

productdf = pd.DataFrame([
    ["Laptop", 20000, 3],
    ["Mobile", 20000, 3]
],
    columns=['Product_name', 'Price', 'Quantity']
)

print("The output is:\n", productdf)

productdf2 = pd.DataFrame([
    ["Mouse", 1600, 17],
    ["Keyboard", 2200, 23]
],
    columns=['Product_name', 'Price', 'Quantity']
    index=[2, 3]
)

productdf3 = productdf._append(productdf2)

print("After adding rows, the final output is:\n", productdf3)

productdf3["Customer Name"] = ["Naman", "Archit", "Bharat", "Shivansh"]

print("After adding columns, The final output is:\n", productdf3)
```

### Deleting rows and columns from the data frame
Rows and columns from the data frame can be deleted using the `drop()`.

Column which need to be deleted from the data frame are specified by the names of the columns as the value of `columns` argument in the `drop` function.

Rows can be deleted by specifying the index of the row to be deleted as the value of `index` argument in the `drop` function.

```python
productdf4 = productdf3.drop(columns=['Price'])

print("After deleting columns, The final output is:\n", productdf4)

productdf4 = productdf3.drop(index=[1])

print("After deleting rows, The final output is:\n", productdf4)
```

### Import of data

The data in real world scenario is not written in python but imported from external sources. The `pandas` library provide many functions to import data from different types of files and store in a `DataFrame`.
The different functions of importing data are as follows:-
1. `read_csv`:- helps to read a csv file
2. `read_excel`:- helps to read an excel file
3. `read_html`:- helps to read an html file
4. `read_json`:- helps to read a json file
5. `read_sql`:- helps to read a sql file


```python
import pandas as pd
student = pd.read_csv("file_path")
print("Dimension", student.shape)
print("size", student.size)
print("preview of dataset", student.columns)

```

### Functions of Data-frame

The pandas library provides man functions with respect to data-frame. These functions are related to information of the data-frame such as:

1. Describe
2. Info
3. Displaying records using head(), tail().
4. Statistical functions including mean, median.
5. Mathematical functions such as min(), prod() and sum().
6. Sorting of the data-frame on the basis of specified column using sort_values().


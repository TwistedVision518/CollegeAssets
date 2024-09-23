# {DAUP} 1. NumPy Library For Arrays

Course: Data Analysis Using Python (Data%20Analysis%20Using%20Python%20f349ea4f18e647ca9ae815226b6a69ff.md)
Confidence: Not Confident
Last Edited: September 9, 2024 11:11 PM

- July 31, 2024
    
    ### Array
    
    - An array is a ***data structure*** that contains a ***group of elements of same datatype*** such as
        - Integer
        - Character
        - String
        - Float
    - Arrays are used to organise data for easy sorting or searching.
    - A specific ***array element is accessed by an index***.
    - In python, ***arrays can be efficiently created using the NumPy library*** which provides many functions for effective programming related to array.
    
    ---
    
    ### Accessing Elements of 1D Array Using Different Functions
    
    We can access array elements by using different functions such as mathematical, statistical, trigonometrical, logarithmic & exponential functions. The detail of all functions are as follows:
    
    1. Modifying an element at specified index.
    2. To identify size of the array.
    3. To identify data type of the element of the array.
    4. To identify mean value of all array elements.
    5. To identify median value of all array elements.
    6. To identify minimum value of all array elements.
    7. To identify maximum value of all array elements.
    8. To calculate the sum of all array elements.
    9. To calculate the product of all array elements.
    10. To perform sorting on all array elements.
    11. To identify square root of all array elements.
    12. To calculate all the elements raised to power of a number.
    13. To calculate the absolute value of all array elements.
    14. To calculate the sine value of all array elements.
    15. To calculate the cosine of all array elements.
    16. To calculate the tangent value of all array elements.
    17. To calculate the log with exponential base of all array elements.
    18. To calculate the log with base 10 of all array elements.
    19. To calculate the exponential value of all array elements.
    - Code
        
        ```python
        import numpy
        
        # The index of 1D array
        myArray = numpy.array([1,2,3,4,5], int)
        print(f"The result is : {myArray[4]}")
        
        # To identify size of the array.
        print(f"The size of the array is : {myArray.size}")
        
        # To identify data type of the element of the array.
        print(f"The data type of the element of the array is : {myArray.dtype}")
        
        # To identify mean value of all array elements.
        print(f"The mean value of all array elements is : {myArray.mean()}")
        
        # To identify median value of all array elements.
        print(f"The median value of all array elements : {numpy.median(myArray)}")
        
        # To identify minimum value of all array elements.
        print(f"The minimum value of all array elements is : {myArray.min()}")
        
        # To identify maximum value of all array elements.
        print(f"The maximum value of all array elements is : {myArray.max()}")
        
        # To calculate sum of all array elements.
        print(f"The sum of all array elements is : {myArray.sum()}")
        
        # To calculate product of all array elements.
        print(f"The product of all array is : {myArray.prod()}")
        
        # To perform sorting on all array elements.
        print(f"The sorted array is : {numpy.sort(myArray)}")
        
        # To identify square root of all array elements.
        print(f"The square root of all array elements is : {numpy.sqrt(myArray)}")
        
        # To calculate all the elements raised to power of a number.
        print(f"The power of all the array elements raised to power of 3 is : {numpy.power(myArray, 3)}")
        
        # To calculate the absolute value of all array elements.
        myArraySign = numpy.array([-1, 0, 1, -2, 3], int)
        print(f"The absolute value of all array elements is : {numpy.absolute(myArraySign)}")
        
        # To calculate the sine value of all array elements.
        print(f"The sine value of all array elements is : {numpy.sin(myArray)}")
        
        # To calculate the cosine value of all array elements.
        print(f"The cosine value of all array elements is : {numpy.cos(myArray)}")
        
        # To calculate the tangent value of all array elements.
        print(f"The tangent value of all array elements is : {numpy.tan(myArray)}")
        
        # To calculate the log with exponential base of all array elements.
        print(f"The log with exponential base of all array elements is : {numpy.log(myArray)}")
        
        # To calculate the log with base 10 of all array elements.
        print(f"The log with base 10 of all array elements is : {numpy.log10(myArray)}")
        
        # To calculate the exponential value of all array elements.
        print(f"The exponential value of all array elements is : {numpy.exp(myArray)}")
        ```
        
        O/P
        
        ```python
        The result is : 5
        The size of the array is : 5
        The data type of the element of the array is : int64
        The mean value of all array elements is : 3.0
        The median value of all array elements : 3.0
        The minimum value of all array elements is : 1
        The maximum value of all array elements is : 5
        The sum of all array elements is : 15
        The product of all array is : 120
        The sorted array is : [1 2 3 4 5]
        The square root of all array elements is : [1.         1.41421356 1.73205081 2.         2.23606798]
        The power of all the array elements raised to power of 3 is : [  1   8  27  64 125]
        The absolute value of all array elements is : [1 0 1 2 3]
        The sine value of all array elements is : [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
        The cosine value of all array elements is : [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
        The tangent value of all array elements is : [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]
        The log with exponential base of all array elements is : [0.         0.69314718 1.09861229 1.38629436 1.60943791]
        The log with base 10 of all array elements is : [0.         0.30103    0.47712125 0.60205999 0.69897   ]
        The exponential value of all array elements is : [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
        ```
        

---

- August 7, 2024
    
    ### Mathematical Operator For 1D Array
    
    We can perform different mathematical operations such as addition, subtraction, multiplication, division ( / ), integer division ( // )& modulus division ( % ).
    
    - Code
        
        ```python
        import numpy
        
        myArray1 = numpy.array([11,22,33], int)
        myArray2 = numpy.array([40,50,60], int)
        myArray3 = numpy.array([7,8,9], int)
        
        # To perform +, -, * operations on two arrays.
        
        myArrayAdd = myArray1 + myArray2
        print(f"Addition : {myArrayAdd}")
        
        myArraySub = myArray1 - myArray3
        print(f"Subtraction : {myArraySub}")
        
        myArrayMul = myArray1 * myArray3
        print(f"Multiplication : {myArrayMul}")
        
        # To perform /, //, % operations on two arrays.
        
        myArrayDiv = myArray2 / myArray1
        print(f"Division : {myArrayDiv}")
        
        myArrayIntDiv = myArray2 // myArray1
        print(f"Integer Division : {myArrayIntDiv}")
        
        myArrayMod = myArray2 % myArray1
        print(f"Modulus : {myArrayMod}")
        ```
        
        O/P
        
        ```python
        Addition : [51 72 93]
        Subtraction : [ 4 14 24]
        Multiplication : [ 77 176 297]
        Division : [3.63636364 2.27272727 1.81818182]
        Integer Division : [3 2 1]
        Modulus : [ 7  6 27]
        ```
        
    
    ---
    
    ### Relational Operators For 1D Array
    
    ### Q : Define all Relational Operators
    
    - == : Equality
    - >    : Greater Than
    - <    : Less Than
    
    - !=  : Not Equal To
    - >= : Greater Than or Equal To
    - <= : Less Than or Equal To
    
    ### Q: Prepare truth Table for logical operator ( AND, OR, NOT )
    
    | i1 | i2 | AND | OR |
    | --- | --- | --- | --- |
    | 0 | 0 | 0 | 0 |
    | 0 | 1 | 0 | 1 |
    | 1 | 0 | 0 | 1 |
    | 1 | 1 | 1 | 1 |
    
    | i | NOT |
    | --- | --- |
    | 1 | 0 |
    | 0 | 1 |
    
    ---
    
    # Multidimensional Array
    
    The simplest form of multidimensional array is 2D array. A 2D array has rows & columns. It can also be considered as a list of 1D arrays.
    
    A 2D array of size of ***[ m ] [ n ]*** can be considered as a tabular form having 
    **‘*m’** no: of rows* & ***‘n’** no: of columns.* Thus a matrix is considered as a specialised 2D array.
    
    ### Creating a Multidimensional Array
    
    A multidimensional array can be created by using the following functions
    
    1. array(  )
    
    1. reshape(  )
    
    1. matrix(  )
    
    1. zeros(  )
    
    1. ones(  )
    
    A 2D array is represented using 2 square brackets for rows & columns and both the square brackets are inside the main square brackets.
    
    $$
    \begin{bmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9\\
    10 & 11 & 12\\
    \end{bmatrix}
    $$
    
    1. Array function uses square bracket outside all elements to denote one row of the array.
    2. Matrix function uses semicolon to separate a row from the other.
    3. Reshape function converts 1D array into multidimensional array on the basis of specified argument for rows & columns.
    4. Zeros & Ones function create multidimensional array of specified dimension & fill them with zeros & ones respectively.
    - Code
        
        ```python
        import numpy
        
        myArray = numpy.array([[100, 200, 300],[400, 500, 600]])
        print(f"Array :\n {myArray}\n")
        
        myArrayMatrix = numpy.matrix('100, 200, 300; 400, 500, 600')
        print(f"Matrix :\n {myArrayMatrix}\n")
        
        arrayToReshape = numpy.array([100, 200, 300, 400, 500, 600]) 
        myArrayReshape = numpy.reshape(arrayToReshape, (3,2))
        print(f"After Reshape :\n {myArrayReshape}\n")
        
        myArrayZeroes = numpy.zeros((4,3))
        print(f"Zeroes :\n {myArrayZeroes}\n")
        
        myArrayOnes = numpy.ones((4,3))
        print(f"Ones :\n {myArrayOnes}\n")
        ```
        
        O/P
        
        ```python
        Array :
         [[100 200 300]
         [400 500 600]]
        
        Matrix :
         [[100 200 300]
         [400 500 600]]
        
        After Reshape :
         [[100 200]
         [300 400]
         [500 600]]
        
        Zeroes :
         [[0. 0. 0.]
         [0. 0. 0.]
         [0. 0. 0.]
         [0. 0. 0.]]
        
        Ones :
         [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]
        ```
        
    
    <aside>
    ❓ For Next Class : Multidimensional array || Relational & Mathematical Operators
    
    </aside>
    
    - Homework Code
        
        ```jsx
        import numpy
        
        myArray1 = numpy.array([[11, 22, 33],[44, 55, 666]], int)
        myArray2 = numpy.array([[40, 50, 60],[70, 80, 90]])
        myArray3 = numpy.array([[5, 6, 7],[8, 9, 10]])
        
        # To perform +, -, * operations on two arrays.
        
        myArrayAdd = myArray1 + myArray2
        print(f"Addition :\n {myArrayAdd}")
        
        myArraySub = myArray1 - myArray3
        print(f"Subtraction :\n {myArraySub}")
        
        myArrayMul = myArray1 * myArray3
        print(f"Multiplication :\n {myArrayMul}")
        
        # To perform /, //, % operations on two arrays.
        
        myArrayDiv = myArray2 / myArray1
        print(f"Division :\n {myArrayDiv}")
        
        myArrayIntDiv = myArray2 // myArray1
        print(f"Integer Division :\n {myArrayIntDiv}")
        
        myArrayMod = myArray2 % myArray1
        print(f"Modulus :\n {myArrayMod}")
        ```
        
        O / P
        
        ```jsx
        Addition :
         [[ 51  72  93]
         [114 135 756]]
        Subtraction :
         [[  6  16  26]
         [ 36  46 656]]
        Multiplication :
         [[  55  132  231]
         [ 352  495 6660]]
        Division :
         [[3.63636364 2.27272727 1.81818182]
         [1.59090909 1.45454545 0.13513514]]
        Integer Division :
         [[3 2 1]
         [1 1 0]]
        Modulus :
         [[ 7  6 27]
         [26 25 90]]
        ```
        

---

- August 14, 2024
    
    ## Accessing Elements in Multidimensional Array
    
    Elements in multidimensional array are accessed using the concept of indexing & slicing.
    
    ---
    
    ### Indexing
    
    Indexing helps to specify the location of the element in an array. An element in 2D array is accessed by using the subscript; i.e. **row-index** & **column-index** of the array.
    
     Every element in the array is identified by an element name of the form:
    
    $$
    myArray[x][y]
    $$
    
    where myArray is the name of the array & *‘x’* & *‘y’* are the subscript corresponding to **row-index** & **column-index** respectively
    
    <aside>
    💡 ***Indexing always starts with 0, not with 1***
    
    </aside>
    
    ---
    
    ### Slicing
    
    A slice represents a part or piece of the array. Slicing in multidimensional array is done by specifying the starting & ending index of both row & column.
    
    It should be noted that in multidimensional array the starting & ending index of rows & columns are separated by ‘ : ’ ( colon ) & row & column are separated by ‘ , ’ ( comma )
    
    **Slicing is done by specifying 4 arguments**:
    
    1. Beginning of row
    2. Ending of row
    
    1. Beginning of column
    2. Ending of column
    
    $$
    [\ beginning\_row\ :\ ending\_row\ ,\ beginning\_col\ :\ ending\_col\ ]
    $$
    
    - Code
        
        ```python
        import numpy
        
        myArray = numpy.reshape(range(100,400,50), (3,2))
        print(f"The array is :\n{myArray}")
        
        # Performing Indexing
        print(f"1st row ; 2nd col : {myArray[0][1]}")
        print(f"2nd row ; 1st col : {myArray[1][0]}")
        print(f"2nd row ; 2nd col : {myArray[1][1]}")
        print(f"3rd row ; 1st col : {myArray[2][0]}")
        print(f"3rd row ; 2nd col : {myArray[2][1]}")
        print("--------------------------------------------------------")
        # Perform Slicing : ROW ONLY
        print(f"First 2 rows :\n{myArray[0:2, ]}\n")
        print(f"3rd row :\n{myArray[2, ]}\n")
        print(f"1st row & 2nd col :\n{myArray[0:2, 0:2]}\n")
        
        print(f"2nd & 3rd row :\n{myArray[1:, 0:2]}\n")
        ```
        
        O / P
        
        ```jsx
        The array is :
        [[100 150]
         [200 250]
         [300 350]]
        1st row ; 2nd col : 150
        2nd row ; 1st col : 200
        2nd row ; 2nd col : 250
        3rd row ; 1st col : 300
        3rd row ; 2nd col : 350
        --------------------------------------------------------
        First 2 rows :
        [[100 150]
         [200 250]]
        
        3rd row :
        [300 350]
        
        1st row & 2nd col :
        [[100 150]
         [200 250]]
        
        2nd & 3rd row :
        [[200 250]
         [300 350]]
        
        ```
        
    
    ---
    
    ## Functions on Multidimensional Array
    
    The following functions are used on multidimensional array such as
    
    ### 1. Transpose:
    
    - Transpose function returns a new matrix whose rows are the columns of the original & vice versa.
    
    ### 2. Diagonal :
    
    - Diagonal function returns the diagonal element of the matrix.
    
    ### 3. Flatten :
    
    - Flatten function returns the 1D array by converting the matrix into 1D array.
    
    ### 4. Shape :
    
    - Shape function returns the shape of the array ( no: of rows & columns ).
    
    ### 5. Sort :
    
    - Sort function helps to sort the array & the excess element determine whether the array will be sorted on row or column.
    - If excess = 0, Sorting will be done on the basis of column.
    - If excess = 1, Sorting will be done on the basis of row.
    - Code
        
        ```jsx
        import numpy
        
        myArray = numpy.reshape(range(100,400,50), (3,2))
        print(f"The array is :\n{myArray}")
        
        print(f"Transposed matrix is   :\n{myArray.transpose()}            \n")
        print(f"Shape of the matrix is :\n{myArray.shape}                  \n")
        print(f"Flattened matrix is    :\n{myArray.flatten()}              \n")
        print(f"Sorted (row) matrix is :\n{numpy.sort(myArray)}            \n")
        print(f"Sorted (col) matrix is :\n{numpy.sort(myArray, axis=0)}    \n")
        print(f"Diagonal elements are  :\n{numpy.diagonal(myArray)}        \n")
        ```
        
        O / P
        
        ```jsx
        The array is :
        [[100 150]
         [200 250]
         [300 350]]
        Transposed matrix is   :
        [[100 200 300]
         [150 250 350]]            
        
        Shape of the matrix is :
        (3, 2)                  
        
        Flattened matrix is    :
        [100 150 200 250 300 350]              
        
        Sorted (row) matrix is :
        [[100 150]
         [200 250]
         [300 350]]            
        
        Sorted (col) matrix is :
        [[100 150]
         [200 250]
         [300 350]]    
        
        Diagonal elements are  :
        [100 250]        
        
        ```
        
    
    ---
    

---
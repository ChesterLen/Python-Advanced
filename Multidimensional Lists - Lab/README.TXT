    1. Sum Matrix Elements
Write a program that reads a matrix from the console and prints:
    • The sum of all numbers in the matrix
    • The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ".

    Examples: 

    Input: 3, 6                 Output: 76
           7, 1, 3, 3, 2, 1             [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
           1, 3, 9, 8, 5, 6
           4, 6, 7, 9, 1, 0

    2. Even Matrix
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested comprehension for that problem. 
On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column separated with a comma and a space ", ".

    Examples:

    Input: 2                       Output: [[2], [4, 6]]
           1, 2, 3
           4, 5, 6

    Input: 4                       Output: [[10, 24], [34, 110], [4, 12], []]
           4
           10, 33, 24, 5, 1
           67, 34, 11, 110, 3
           4, 12, 33, 63, 21
           557, 45, 23, 55, 67

    3. Flattening Matrix
Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column separated with a comma and a space ", ".

    Examples:
    
    Input: 2               Output: [1, 2, 3, 4, 5, 6]
           1, 2, 3
           4, 5, 6

    Input: 3               Output: [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]
           10, 2, 21, 4
           5, 20, 41, 9
           6, 2, 4, 99

    4. Sum Matrix Columns
Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space.

    Examples:

    Input: 3, 6            Output: 12
           7 1 3 3 2 1             10
           1 3 9 8 5 6             19
           4 6 7 9 1 0             20
                                   8
                                   7

    Input: 3, 3            Output: 12
           1 2 3                   15
           4 5 6                   18
           7 8 9

    5. Primary Diagonal
Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for each column - N numbers, separated by a single space. 

    Examples:

    Input: 3          Output: 4
           11 2 4
           4 5 6
           10 8 -12
           (You have to collect: 11 + 5 + -12 = 4)

    Input: 3          Output: 15
           1 2 3
           4 5 6
           7 8 9
           (You have to collect: 1 + 5 + 9 = 15)
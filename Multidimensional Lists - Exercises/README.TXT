    1. Diagonals
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

    Example:
    
    Input: 3        Output: Primary diagonal: 1, 5, 9. Sum: 15
           1, 2, 3          Secondary diagonal: 3, 5, 7. Sum: 15
           4, 5, 6
           7, 8, 9

    2. Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. 
Print the absolute difference between the primary and the secondary diagonal sums.

    Examples:

    Input: 3             Output: 15
           11 2 4
           4 5 6
           10 8 -12

           Primary diagonal: sum = 11 + 5 + (-12) = 4
           Secondary diagonal: sum = 4 + 5 + 10 = 19
           Difference: |4 - 19| = 15

    Input: 4              Output: 34
           -7 14 9 -20
           3 4 9 21
           -14 6 8 44

    3. 2x2 Squares in Matrix
Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". 
On the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.

    Examples:

    Input: 3 4        Output: 2
           A B B D
           E B B B
           I J B B

           Two 2x2 squares of equal cells.

    Input: 2 2          Output: 0
           a b
           c d

           No 2x2 squares of equal cells exist.

    Input: 5 4          Output: 3
           A A B D
           A A B B
           I J B B
           C C C G
           C C K P

           Three 2x2 squares of equal cells.

    4. Maximal Sum
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. 
There will be no case with two or more 3x3 squares with equal maximal sum.
Input
    • On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
    • On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
Output
    • On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
    • On the following 3 lines, print each element of the found submatrix, separated by a single space

    Examples:

    Input: 4 5           Output: Sum = 75
           1 5 5 2 4             1 4 14
           2 1 4 14 3            7 11 2
           3 7 11 2 8            8 12 16
           4 8 12 16 4

    Input: 5 6            Output: Sum = 34
           1 0 4 3 1 1            2 5 6
           1 3 1 3 0 4            5 4 1
           6 4 1 2 5 6            6 0 5
           2 2 1 5 4 1
           3 3 3 6 0 5

    5. Matrix of Palindromes
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
    • Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
    • Columns + rows define the middle letter: 
        ◦ column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
        ◦ column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
    • The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
    • r and c are integers in the range [1, 26]

    Examples: 
    
    Input: 4 6          Output: aaa aba aca ada aea afa
                                bbb bcb bdb beb bfb bgb
                                ccc cdc cec cfc cgc chc
                                ddd ded dfd dgd dhd did

    Input: 3 2          Output: aaa aba
                                bbb bcb
                                ccc cdc
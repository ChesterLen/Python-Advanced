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
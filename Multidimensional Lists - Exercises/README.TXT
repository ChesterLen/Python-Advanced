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

    6. Matrix Shuffling
Write a program that reads a matrix from the console and performs certain operations with its elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data. 
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. 
A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
    • If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly). 
    • If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. 
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

    Examples:

    Input: 2 3            Output: 5 2 3
           1 2 3                  4 1 6
           4 5 6                  Invalid input!
           swap 0 0 1 1           5 4 3
           swap 10 9 8 7          2 1 6
           swap 0 1 1 0
           END

    Input: 1 2             Output: Invalid input!
           Hello World             World Hello
           0 0 0 1                 Invalid Input!
           swap 0 0 0 1
           swap 0 1 0 0
           END

    7. Snake Moves
You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M. 
A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end. 
The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
    • On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}". 
    • On the second line, you will receive the string representing the snake
Output
    • You should print the snake's zigzag path of size N x M (rows x columns)

    Examples:

    Input: 5 6      Output: SoftUn
           SoftUni          UtfoSi
                            niSoft
                            foSinU
                            tUniSo

    Input: 1 4      Output: Pyth
           Python

    8. Bombs
You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals). One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).
Input
    • On the first line, you are given the integer N - the size of the square matrix.
    • The following N lines hold each column's values - N numbers separated by a space.
    • On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
    • On the first line, you need to print the count of all alive cells in the format: 
"Alive cells: {alive_cells}"
    • On the second line, you need to print the sum of all alive cells in the format: 
"Sum: {sum_of_cells}"
    • In the end, print the matrix. A space must separate the cells.

    Examples:

    Input: 4         Output: Alive cells: 3
           8 3 2 5           Sum: 12
           6 4 7 9           8 -4 -5 -2
           9 9 3 6           -3 -3 0 2
           6 8 1 2           0 0 -4 -1
           1,2 2,1 2,0       -3 -1 -1 2

    Input: 3                 Alive cells: 3
           7 8 4             Sum: 8
           3 1 5             4 1 0
           6 4 9             0 -3 -8
           0,2 1,0 2,2       3 -8 0

    9. Miner
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move. 
On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down". 
In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
    • * - a regular position on the field
    • e - the end of the route
    • c - coal
    • s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. 
If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
    • If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
    • If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
    • If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
    • Field size - an integer number
    • Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
    • The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
Output
    • There are three types of output as mentioned above.

    Examples:

    Input: 5                                                  Output: Game over! (1, 3)
           up right right up right
           * * * c *
           * * * e *
           * * c * *
           s * * c *
           * * c * *

    Input: 4                                                   Output: You collected all coal! (2, 3)
           up right right right down
           * * * e
           * * c *
           * s * c
           * * * *

    Input: 6                                                    Output: 3 pieces of coal left. (5, 0)
           left left down right up left left down down down
           * * * * * *
           e * * * c *
           * * c s * *
           * * * * * *
           c * * * c *
           * * c * * *
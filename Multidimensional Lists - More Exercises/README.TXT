    1. Flatten Lists
Write a program to flatten several lists of numbers received in the following format:
    • String with numbers or empty strings separated by "|"
    • Values are separated by spaces (" ", one or several)
    • Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below:

    Examples:

    Input: 1 2 3 |4 5 6 |  7  88      Output: 7 88 4 5 6 1 2 3
    
    Input: 7 | 4  5|1 0| 2 5 |3       Output: 3 2 5 1 0 4 5 7

    Input: 1| 4 5 6 7  |  8 9         Output: 8 9 4 5 6 7 1

    2. Matrix Modification
Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. 
You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
    • "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
    • "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

    Examples:

    Input: 3                  Output: 6 2 3
           1 2 3                      4 3 6
           4 5 6                      7 8 9
           7 8 9Add 0 0 5
           Subtract 1 1 2
           END

    Input: 4                   Output: Invalid coordinates
           1 2 3 4                     Invalid coordinates
           5 6 7 8                     -41 2 3 4
           8 7 6 5                     5 6 7 8
           4 3 2 1                     8 7 6 5
           Add 4 4 100                 4 3 2 101
           Add 3 3 100
           Subtract -1 -1 42
           Subtract 0 0 42
           END

    3. Knight Game
Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated. 
It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left. 
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.
Input
    • On the first line, you will receive integer N - the size of the board
    • On the following N lines, you will receive strings with "K" and "0"
Output
    • Print a single integer with the number of knights that need to be removed.

    Examples:

    Input: 5           Output: 1
           0K0K0
           K000K
           00K00
           K000K
           0K0K0

    Input: 2           Output: 0
           KK
           KK

    Input: 8           Output: 12
           0K0KKK00
           0K00KKKK
           00K0000K
           KKKKKK0K
           K0K0000K
           KK00000K
           00K0K000
           000K00KK

    4. Easter Bunny
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
    • One bunny - randomly placed in it and marked with the symbol "B"
    • Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. 
The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. 
For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
    • A number representing the size of the field
    • The matrix representing the field (each position separated by a single space)
Output
    • The direction which should be considered as best (lowercase)
    • The field positions from which we are collecting eggs as lists
    • The total number of eggs collected

    Examples:
    
    Input: 5                      Output: right
           1 3 7 9 11                     [3, 1]
           X 5 4 X 63                     [3, 2]
           7 3 21 95 1                    [3, 3]
           B 1 73 4 9                     [3, 4]
           9 2 33 2 0                     87

    Input: 8                       Output: down
           4 18 9 7 24 41 52 11            [6, 2]
           54 21 19 X 6 34 75 57           [7, 2]
           76 67 7 44 76 27 56 37          113
           92 35 25 37 52 34 56 72
           35 X 1 45 4 X 37 63
           105 X B 2 12 43 5 19
           48 19 35 20 32 27 42 4
           73 88 78 32 37 52 X 22
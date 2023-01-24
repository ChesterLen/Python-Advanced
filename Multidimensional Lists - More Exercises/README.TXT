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
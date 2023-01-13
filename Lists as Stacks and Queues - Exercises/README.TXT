    1. Reverse Numbers
Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack.
Print the reversed integers on one line, separated by a single space.

    Examples:

    Input: 1 2 3 4 5     Output: 5 4 3 2 1

    Input: 1             Output: 1

    2. Stacked Queries
You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
    • '1 {number}' – push the number (integer) into the stack
    • '2' – delete the number at the top of the stack
    • '3' – print the maximum number in the stack
    • '4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"

    Examples:

    Input: 9        Output: 26
           1 97             20
           2                91, 20, 26
           1 20
           2
           1 26
           1 20
           3
           1 91
           4

    Input: 10       Output: 8, 16, 25, 32, 66, 47
           2
           1 47
           1 66
           1 32
           4
           3
           1 25
           1 16
           1 8
           4

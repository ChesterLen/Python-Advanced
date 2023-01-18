    1. Unique Usernames
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. 
On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):

    Examples:

    Input: 6            Output: George
           George               Peter
           George               NiceGuy1234
           George
           Peter
           George
           NiceGuy1234

    Input: 10            Output: Peter
           Peter                 Maria
           Maria                 George
           Peter                 Steve
           George                Alex
           Steve
           Maria
           Alex
           Peter
           Steve
           George

    2. Sets of Elements
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated by a single space - representing the lengths of two separate sets. 
On the next n + m lines, you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. 
Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}

    Examples:

    Input: 4 3     Output: 3
           1               5
           3
           5
           7
           3
           4
           5

    Input: 2 2     Output: 1
           1
           3
           1
           5
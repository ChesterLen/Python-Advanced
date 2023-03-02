    1.Scheduling
You are hired to create a program that implements SJF (Shortest Job First). It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) separated by comma and space ", ".
On the second line you will be given the index of the job that we are interested in and want to know how many cycles will pass until the job is done.
The tasks that need the least amount of clock-cycles will be completed first. 
For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
You have to print how many clock-cycles will pass until the task you are interested in is completed. For more clarifications, see the examples below.
Input
    • On the first line you will receive numbers separated by ", "
    • On the second line you will receive the index of the task you are interested in
Output
    • Single line: the clock-cycles that will pass until the task you are interested in is finished

    Examples:

    Input: 3, 1, 10, 1, 2         Output: 7
           0

    Input: 4, 10, 10, 6, 2, 99    Output: 32
           2

    2.Checkmate
You will be given a chess board (8x8). On the board there will be 3 types of symbols:
    • "." – empty square
    • "Q" – a queen
    • "K" – the king
Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the knight).
Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king. For more clarification see the examples.
Input
    • 8 lines – the state of the board (each square separated by single space)
Output
    • The positions of the queens that can capture the king as lists
    • If the king cannot be captured, print: "The king is safe!"
    • The order of output does not matter
Constrains
    • There will always be exactly 8 lines
    • There will always be exactly one King
    • Only the 3 symbols described above will be present in the input

    Examples:

    Input: . . . . . . . .     Output: [2, 5]
           Q . . . . . . .             [5, 1]
           . K . . . Q . .             [1, 0]
           . . . Q . . . .
           Q . . . Q . . .
           . Q . . . . . .
	   . . . . . . Q .
	   . Q . Q . . . .

    Input: . . . . . . . .     Output: The king is safe!
           . . . Q . . . .
	   . . . . . . . .
	   . . . . . . . .
	   Q . . . Q . . .
	   . . K . . . . .
	   . . . . . . Q .
	   . . . Q . . . .

    3.List Pureness
Write function called best_list_pureness which will receive a list of numbers and a number K.
You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated by summing all the elements in the list multiplied by their indices).
For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
At the end the function should return a string containing the highest pureness and the amount of rotations that were made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations".
If there is more than one highest pureness, take the first one.
Note: Submit only the function in the judge system
Input
    • There will be no input, just parameters passed to your function
Output
    • There is no expected output
    • The function should return a string in the following format: "Best pureness {pureness_value} after {count_rotations} rotations"
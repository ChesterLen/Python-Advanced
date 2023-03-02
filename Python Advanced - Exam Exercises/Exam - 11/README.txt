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
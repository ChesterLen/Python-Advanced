    1.  Stewards
"It's only when you are flying above that you realize how incredible the Earth really is."
As you know, stewards are needed for every single flight. Today you will be that one steward, and you will be assisting the passengers in finding their seats.
You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}". You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. Next, take the sum of those two numbers and find its ASCII character.
    • Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
    • If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
    • If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.
The program should end under the following circumstances:
    • You have found 3 (three) seat matches 
    • You have made a total of 10 rotations
Input
    • On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
    • On the second and the third line, you will be given two more sequences - integers separated by a comma and a space ", "
Output
When the program ends, print the following on two different lines:
    • Seat matches: {matches separated by comma and space}
    • Rotations count: {total rotations made}

    Examples:

    Input: 17K, 20B, 3C, 15D, 31Z, 28F       Output: Seat matches: 20B, 15D, 3C
           20, 35, 15, 3, 2, 10                      Rotations count: 4
           1, 15, 64, 53, 45, 46

    Input: 25A, 16B, 44T, 49D, 27M, 44F      Output: Seat matches: 25C, 40E, 15C
           15, 25, 80, 40, 15, 99, 52                Rotations count: 7
           15, 42, 29
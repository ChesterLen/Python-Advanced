    1. Numbers
First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
    • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
    • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
    • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
    • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
    • "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.

    Examples:

    Input: 1 2 3 4 5               Output: True
           1 2 3                           1, 2, 3, 4, 5, 6
           3                               1, 2, 3
           Add First 5 6
           Remove Second 8 9 11
           Check Subset

    Input: 5 4 2 9 9 5 4                   False
           1 1 1 5 6 5                     2, 3, 4, 5, 6, 9
           4                               6
           Add First 5 6 9 3
           Add Second 1 2 3 3 3
           Check Subset
           Remove Second 1 2 3 4 5

    2. Expression Evaluator
Write a program that evaluates a string expression. You will be given that string expression on the first line in the form of numbers and operators separated with a single space from each other. 
Your job is to take that string expression and calculate the result after evaluating it.
To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", the first time we meet an operator (*), we should take all the numbers we have so far (2, 4), apply that operation to them, and save the result (8). 
The next time we meet an operator (-), we again take all the numbers we have (8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). In the end, we print the result.
All the numbers will always be integers, and the possible operators are "*", "+", "-", "/". It is important to keep the order of the numbers (especially for "/" and "-" because the order matters). 
When having a division, you should round the result to the lower integer.
Input
    • Single line: a string containing integers and operators
Output
    • Single number: the result after the evaluation

    Examples:

    Input: 6 3 - 2 1 * 5 /                         Output: 1

    Input: 2 2 - 1 *                                Output: 0

    Input: 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *    Output: 164

    3. Milkshakes
You are learning how to make milkshakes.
First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
Input
    • On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
    • On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
    • On the first line, print:
        ◦ If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
        ◦ Otherwise: "Not enough milkshakes."
    • On the second line - print:
        ◦ If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
        ◦ Otherwise: "Chocolate: empty"
    • On the third line - print:
        ◦ If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
        ◦ Otherwise: "Milk: empty"

    Examples:

    Input: 20, 24, -5, 17, 22, 60, 26         Output: Great! You made all the chocolate milkshakes needed!
           26, 60, 22, 17, 24, 10, 55                 Chocolate: 20
                                                      Milk: 10, 55

    Input: -10, -2, -30, 10                   Output: Not enough milkshakes.
           -5                                         Chocolate: -10, -2, -30, 10
                                                      Milk: empty

    Input: 2, 3, 3, 7, 2                      Output: Great! You made all the chocolate milkshakes needed!
           2, 7, 3, 3, 2, 14, 6                       Chocolate: empty
                                                      Milk: 14, 6
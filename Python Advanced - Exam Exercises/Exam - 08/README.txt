    1. Pizza Orders
On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas, separated by comma and space ", ".
On the second line, you will receive a sequence of employees with pizza-making capacities (how much pizzas an employee could make), separated by comma and space ", ".
Your task is to check if all pizza orders are completed. 
To do that, you should take the first order and the last employee and see:
    • If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order is completed. Remove both the order and the employee.
    • If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining pizzas from the order are going to be made by the next employees until the order is completed. 
        ◦ If there are no more employees to finish the order, consider it not completed.
    • The restaurant does not take orders for more than 10 pizzas at once.
    • If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee. 
You should keep track of the total pizzas that are being made.
Input
    • On the first line you will be given a sequence of pizza orders each represented as a number – integers separated by comma and space ", "
    • On the second line you will be given a sequence of employees with pizza-making capacities – integers separated by comma and space ", "
Output
    • If all orders are successfully completed, print:
All orders are successfully completed!
Total pizzas made: {total count}
Employees: {left employees joined by ", "}
    • Otherwise, if you ran out of employees and there are still some orders left print:
Not all orders are completed.
Orders left: {left orders joined by ", "}

    Examples:

    Input: 11, 6, 8, 1                  Output: All orders are successfully completed!
           3, 1, 9, 10, 5, 9, 1                 Total pizzas made: 15
	                                        Employees: 3, 1

    Input: 10, 9, 8, 7, 5               Output: Not all orders are completed.
           5, 10, 9, 8, 7                       Orders left: 2, 5

    Input: 12, -3, 14, 3, 2, 0          Output: All orders are successfully completed!
           10, 15, 4, 6, 3, 1, 22, 1            Total pizzas made: 5
						Employees: 10, 15, 4, 6

    2. Darts
You will be given a matrix with 7 rows and 7 columns representing the dartboard.
Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the player’s total score.
The first player who reduces their score to zero or less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
    • If a player hits outside the dartboard, he does not score any points.
    • If a player hits a number, it is deducted from his total.
    • If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
    • If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
    • "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
Your job is to find who won the game and with how many turns.
Input
    • The name of the first player and the name of the second player, separated by ", "
    • 7 lines – the dartboard (separated by single space)
    • On the next lines - the coordinates in the format: "({row}, {column})"
Output
    • You should print only one line containing the winner and his count of throws: 
"{name} won the game with {count_turns} throws!"
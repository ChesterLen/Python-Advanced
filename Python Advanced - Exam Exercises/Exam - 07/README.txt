    1. Fireworks Show
Maria wants to make a firework show for the wedding of her best friend. 
We should help her to make the perfect firework show.

First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another sequence of integers representing explosive power.
You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their values is:
    • divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
    • divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
    • divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the same explosive power with the next firework effect. 
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other. 
When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive power, you need to stop mixing. 
To make the perfect firework show, Maria needs 3 of each of the firework types.
Input
    • On the first line, you will receive the integers representing the firework effects, separated by ", ".
    • On the second line, you will receive the integers representing the explosive power, separated by ", ".
Output
    • On the first line, print:
        ◦ if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
        ◦ if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
    • On the second line, print all firework effects left if there are any: 
    • "Firework Effects left: {effect1}, {effect2}, (…)"
    • On the third line, print all explosive fillings left if there are any: 
    • " Explosive Power left: {filling1}, {filling2}, (…)"
    • Then, you need to print all fireworks and the amount you have of them:
        ◦ "Palm Fireworks: {count}"
        ◦ "Willow Fireworks: {count}"
        ◦ "Crossette Fireworks: {count}"

    Examples:

    Input: 5, 6, 4, 16, 11, 5, 30, 2, 3, 27        Output: Congrats! You made the perfect firework show!
           1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22            Palm Fireworks: 4
							   Willow Fireworks: 3
							   Crossette Fireworks: 3

    Input: -15, -8, 0, -16, 0, -22                         Sorry. You can't make the perfect firework show.
           10, 5                                           Explosive Power left: 10, 5
							   Palm Fireworks: 0
							   Willow Fireworks: 0
							   Crossette Fireworks: 0

    2. Collecting Coins
You are playing a game, and your goal is to collect 100 coins.
On the first line, you will be given a number representing the size of the field with a square shape. On the following few lines, you will be given the field with: 
    • One player - randomly placed in it and marked with the symbol "P"
    • Numbers for coins placed at different positions of the field
    • Walls marked with "X"
After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it. 
The player moves in the given direction with one step for each command and collects all the coins that come across.
If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins just once (the first time).
There are only two possible outcomes of the game:
    • The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
    • The player collects at least 100 coins and wins the game.
For more clarifications, see the examples below.
Input
    • A number representing the size of the field (matrix NxN)
    • A matrix representing the field (each position separated by a single space)
    • On each of the following lines, you will get a move command.
Output
    • If the player won the game, print: "You won! You've collected {total_coins} coins."
    • If the player loses the game, print: "Game over! You've collected {total_coins} coins."
    • Collected coins have to be rounded down to the next-lowest number.
    • The player's path as cooridnates in lists on separate lines: 
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"

    Examples:

    Input: 5                          Output: You won! You've collected 125 coins.
           1 X 7 9 11             	      Your path:
           X 14 46 62 0           	      [3, 0]
           15 33 21 95 X          	      [3, 4]
           P 14 3 4 18            	      [3, 0]
           9 20 33 X 0            	      [3, 1]
	   left                   	      [2, 1]
	   right                  	      [1, 1]
	   right                  	      [1, 2]
	   up
	   up
	   right

    Input: 8                           Output: Game over! You've collected 0 coins.
           13 18 9 7 24 41 52 11               Your path:
	   54 21 19 X 6 4 75 6                 [5, 2]
	   76 5 7 1 76 27 2 37                 [4, 2]
	   92 3 25 37 52 X 56 72               [5, 2]
	   15 X 1 45 45 X 7 63                 [4, 2]
	   1 63 P 2 X 43 5 1                   [4, 1]
	   48 19 35 20 100 27 42 80
	   73 88 78 33 37 52 X 22
	   up
	   down
	   up
	   left

    3. Cupcake Shop
Maria is opening a cupcake shop. Help her manage her inventory to improve stock availability.

Write a function called stock_availability which receives:
    • an inventory list of boxes with different kinds of cupcake flavours
    • "delivery" or "sell" as second parameter
    • there might or might not be any other parameters – numbers or strings at the end

In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
    • You should add the boxes at the end of the inventory list
    • There will be always at least one box delivered
In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
    • If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
    • If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s
Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid
    • If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list

    Test code: print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))            Output: ['choco', 'vanilla', 'banana', 'caramel', 'berry']
	       print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))                 ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
	       print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))                                        ['vanilla', 'banana']
	       print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))                                     []
	       print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))                         ['banana']
	       print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))                            ['cookie', 'banana']
	       print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))                              ['chocolate', 'vanilla', 'banana']
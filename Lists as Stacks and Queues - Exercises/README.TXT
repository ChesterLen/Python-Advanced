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

    3. Fast Food
You have a fast-food restaurant, and the food you are offering is previously prepared.
Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who the client with the biggest order for that day is.
First, you will be given the quantity of the food you have for the day (an integer number).
Next, you will be given a sequence of integers (separated by a single space), each representing the quantity of food in each order.
Keep the orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. Before each order, check if you have enough food left to complete it:
    • If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
    • Otherwise, stop serving.
Input
    • On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
    • On the second line, you will receive a sequence of integers, representing each order, separated by a single space
Output
    • On the first line, print the quantity of the biggest order
    • On the second line:
        ◦ If you succeeded in servicing all your clients, print: "Orders complete".
        ◦ Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".

        Examples:

        Input: 348                               Output: 54
               20 54 30 16 7 9                           Orders complete

        Input: 499                                Output: 100
               57 45 62 70 33 90 88 76 100 50             Orders left: 76 100 50

    5. Truck Tour
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). For each petrol pump, you will receive two pieces of information (separated by a single space): 
    • The amount of petrol the petrol pump will give you
    • The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. You never miss filling its tank at a petrol pump.
Input:
    • On the first line, you will receive the number of petrol pumps - N
    • On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between that petrol pump and the next petrol pump, separated by a single space
Output:
    • An integer which will be the smallest index of a petrol pump from which you can start the tour

    Examples:

    Input: 3      Output: 1
           1 5
           10 3
           3 4

    Input: 5      Output: 0
           22 5
           14 10
           52 7
           21 12
           36 9
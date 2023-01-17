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

    4. Fashion Boutique
You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. On the following line, you will be given an integer representing the capacity for one rack in your store.  
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
    • If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box). 
    • If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Input
    • On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a single space.
    • On the second line, you will be given an integer representing the capacity of a rack.
Output
    • Print the number of racks needed to hang up the clothes from the box.

    Examples:

    Input: 5 4 8 6 3 8 7 7 9               Output: 5
           16

    Input: 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6   Output: 5
           20

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

    6. Balanced Parentheses
You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. 
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. 
There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
    • On a single line, you will receive a sequence of parentheses.
Output 
    • For each test case, print on a new line "YES" if the parentheses are balanced. 
    • Otherwise, print "NO"

    Examples:

    Input: {[()]}          Output: YES
    
    Input: {[(])}          Output: NO

    Input: {{[[(())]]}}    Output: YES

    7. *Robotics
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
    • On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
    • On the second line, you will get the starting time in the format "hh:mm:ss"
    • Next, until the "End" command, you will get a product on each line.
Output 
    • Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

    Examples:

    Input: ROB-15;SS2-10;NX8000-3         Output: ROB - detail [08:00:01]
           8:00:00                                SS2 - glass [08:00:02]
           deatil                                 NX8000 - wood [08:00:03]
           wood                                   NX8000 - apple [08:00:06]
           apple
           End

    Input: ROB-8                           Output: ROB - detail [08:00:00]
           7:59:59                                 ROB - wood [08:00:08]
           deatil                                  ROB - glass [08:00:16]
           glass                                   ROB - sock [08:00:24]
           wood
           sock
           End

    8. Crossroads
The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice, and they're going to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is still going to run into some problems, and the first one is getting to the airport. Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely.
Sam is on a single lane of cars that queue until the light goes green. When it does, they start passing one by one on a flashing green light and during the free window before the intersecting road's light goes green. For each second, only one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads when the free window ends, it will get hit at the first character that is still in the crossroads.
Input
    • On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
    • On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
    • On the following lines, until you receive the "END" command, you will receive one of two things:
        ◦ A car - a string containing the model of the car, or
        ◦ The command "green" that indicates the start of a green light cycle
A green light cycle goes as follows:
    • During the green light, cars will enter and exit the crossroads one by one
    • During the free window, cars will only exit the crossroads
Output
    • If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {character_hit}."
    • If everything goes smoothly and you receive an "END" command, print:
"Everyone is safe."
"{total_cars_passed} total cars passed the crossroads."

    Examples:

    Input: 10           Output: Everyone is safe.
           5                    3 total cars passed the crossroads.
           Mercedes
           green
           Mercedes
           BMW
           Skoda
           green
           END

    Input: 9             Output: A crash happened!
           3                     Hummer was hit at e.
           Mercedes
           Hummer
           green
           Hummer
           Mercedes
           green
           END
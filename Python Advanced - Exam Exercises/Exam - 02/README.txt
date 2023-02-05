    1. Energy Drinks

Your friend Stamat is working on a new AI program. Like every irresponsible teenager, he programs all night and, of course, drinks a lot of energy drinks. Stamat's friends are concerned about him and want you to create a program that tells him when to stop the energy drinks and start drinking water.
On the first line, you will receive a sequence of numbers representing milligrams of caffeinе. On the second line, you will receive another sequence of numbers representing energy drinks. It is important to know that the maximum caffeine Stamat can have for the night is 300 milligrams, and his initial is always 0.
To calculate the caffeine in the drink take the last milligrams of caffeinе and the first energy drink, and multiply them. Then, compare the result with the caffeine Stamat drank:
    • If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams, remove both the milligrams of caffeinе and the drink from their sequences. Also, add the caffeine to Stamat's total caffeine.
    • If Stamat is about to exceed his maximum caffeine per night, do not add the caffeine to Stamat’s total caffeine. Remove the milligrams of caffeinе and move the drink to the end of the sequence. Also, reduce the current caffeine that Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).
Stop calculating when you are out of drinks or milligrams of caffeine.
For more clarification, see the examples below.
Input
    • In the first line, you will be given a sequence of the milligrams of caffeinе - integers separated by comma and space ", " in the range [1, 50]
    • In the second line, you will be given a sequence of energy drinks - integers separated by comma and space ", " in the range [1, 300]
Output
    • On the first line:
        ◦ If Stamat hasn't drunk all the energy drinks, print the remaining ones separated by a comma and a space ", ": 
            ▪ "Drinks left: { remaining drinks separated by ", " }"
    • If Stamat has drunk all the energy drinks, print:
        ◦ "At least Stamat wasn't exceeding the maximum caffeine."
    • On the next line, print:
        ◦ "Stamat is going to sleep with { current caffeine } mg caffeine."

    Examples:

    Input: 34, 2, 3                      Output: Drinks left: 100, 250
           40, 100, 250                          Stamat is going to sleep with 60 mg caffeine.

    Input: 1, 16, 8, 14, 5               Output: At least Stamat wasn't exceeding the maximum caffeine.
           27, 23                                Stamat is going to sleep with 289 mg caffeine.

    Input: 1, 23, 2, 1, 42, 22, 7, 14    Output: At least Stamat wasn't exceeding the maximum caffeine.
           51, 100, 3, 7                         Stamat is going to sleep with 264 mg caffeine.

    2. Rally Racing

It's time for one of the biggest races in the world, Paris-Dakar. The organizers of the event want you to do a program that helps them track the cars through the separate stages in the event.

On the first line, you will be given an integer N, which represents the size of a square matrix. On the second line you will receive the racing number of the tracked race car.
On the next N lines you will be given the rows of  the matrix (string sequences, separated by whitespace), which will be representing the race route. The tracked race car always starts with coordinates [0, 0].
Thеre will be a tunnel somewhere across the race route. If the race car runs into the tunnel , the car goes through it and exits at the other end. There will be always two positions marked with "T"(tunnel). The finish line will be marked with "F". All other positions will be marked with ".".
Keep track of the kilometers passed. Every time the race car receives a direction and moves to the next position of the race route, it covers 10 kilometers. If the car goes through the tunnel, it covers NOT 10, but 30 kilometers.
On each line, after the matrix is given, you will be receiving the directions for the race car.
    • left
    • right
    • up
    • down
The race car starts moving across the race route:
    • If you receive "End" command, before the race car manages to reach the finish line, the car is disqualified and the following output should be printed on the Console: "Racing car {racing number} DNF."
    • If the race car comes across a position marked with ".". The car passes 10 kilometers for the current move and waits for the next direction.
    • If the race car comes across a position marked with "T" this is the tunnel. The race car goes through it and moves to the other position marked with  "T" (the other end of the tunnel).
The car passes 30 kilometers for the current move. The tunnel stays behind the car, so the race route is clear, and both the positions marked with "T", should be marked with ".".
    • If the car reaches the finish line - "F" position, the race is over. The tracked race car manages to finish the stage and the following output should be printed on the Console: "Racing car {racing number} finished the stage!". Don’t forget that the car has covered another 10 km with the last move.
Input
    • On the first line you will receive N - the size of the square matrix (race route)
    • On the second line you will receive the racing number of the tracked car
    • On the next N lines, you will receive the race route (elements will be separated by a space).
    • On the following lines, you will receive directions (left, right, up, down).
    • On the last line, you will receive the command "End".
Output
    • If the racing car has reached the finish line before the "End" command is given, print on the Console: "Racing car {racing number} finished the stage!"
    • If the "End"  command is given and the racing car has not reached the finish line yet, the race ends and the following message is printed on the Console: "Racing car {racing number} DNF."
    • On the second line, print the distance that the tracked race car has covered: "Distance covered {kilometers passed} km." 
    • At the end, mark the last known position of the race car with "C" and print the final state of the matrix (race route). The row elements in the output matrix should NOT be separated by a whitespace.

    Examples:

    Input: 5                           Output: Racing car 01 finished the stage!
           01                                  Distance covered 80 km.
           . . . . .                           .....
           . . . T .                           .....
           . . . . .                           .....
           . T . . .                           .....
           . . F . .                           ..C..
           down
           right
           right
           right
           down
           right
           up
           down
           right
           up
           End

    Input: 10                          Output: Racing car 45 DNF.
           45                                  Distance covered 100 km.
           . . . . . . . . . .                 ..........
           . . T . . . . . . .                 ..........
           . . . . . . . . . .                 ..........
           . . . . . . . . . .                 ......F...
           . . . . . . . . . .                 ......C...
           . . . . . . . . . .                 ..........
           . . . . . . . T . .                 ..........
           right
           down
           down
           right
           up
           left
           up
           up
           End

    3. Hourly Forecast
Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can see the most sights.
Patricia is busy at work and doesn't have time to think about the perfect place for her vacation, so she wants your help.
Write a function called forecast that stores information about the weather, and returns sorted information for all locations.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the location, and the second one is the weather:
    • Location name: string
        ◦ any string
    • Weather: string
        ◦ "Sunny"
        ◦ "Rainy"
        ◦ "Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations with cloudy weather, and last are the locations with rainy weather.
For each sequence of locations (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
    • There will be no input from the console, just parameters passed to your function
Output
    • The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"

    Examples:

    Test code: print(forecast(               Output: New York - Sunny
                   ("Sofia", "Sunny"),               Sofia - Sunny
                   ("London", "Cloudy"),             London - Cloudy
                   ("New York", "Sunny")))

    Test code: print(forecast(               Output: Beijing - Sunny
                   ("Beijing", "Sunny"),             Bourgas - Sunny
                   ("Hong Kong", "Rainy"),           Peru - Sunny
                   ("Tokyo", "Sunny"),               Tokyo - Sunny
                   ("Sofia", "Cloudy"),              Florence - Cloudy
                   ("Peru", "Sunny"),                Sofia - Cloudy
                   ("Florence", "Cloudy"),           Hong Kong - Rainy
                   ("Bourgas", "Sunny")))

    Test code: print(forecast(               Output: Sofia - Rainy
                   ("Tokyo", "Rainy"),               Tokyo - Rainy
                   ("Sofia", "Rainy")))
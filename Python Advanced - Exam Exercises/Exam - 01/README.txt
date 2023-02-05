    01. Climb the Peaks
Alex is a vlogger and he wants to make videos of climbing the five highest peaks in Pirin mountain in just one week.  He will take his video set, a tent, and his backpack to the mountain.
The backpack fits food portions for one week, exactly. His daily stamina is also limited. 
Your task is to trace his adventure and create a post for his profile @alaroundtheworld, at the end of the journey.
You will have to keep information for all the conquered peaks if any.
Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
First, you will be given a sequence of numbers, representing the quantities of the daily portions of food supplies in his backpack.
Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he will have at his disposal for the next seven days.
You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina. He will start climbing from the first peak in the table below to the last one.
    • If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below, it means that the peak is conquered. 
In this case, you should remove both quantities from the sequences and continue with the next ones towards the next peak.
    • If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak remains unconquered. You should remove both quantities from the sequences. 
Alex will have to sleep in his tent. On the next day, he will try the same peak once again.

    Mountain Peaks: Vihren           Difficulty level: 80
                    Kutelo                             90
                    Banski Suhodol                     100
                    Polezhan                           60
                    Kamenitza                          70

Alex will try to conquer as many peaks as he can in seven days. If he manages to climb all the peaks, the journey ends and the output is printed on the Console.
Finally, print on the Console all the conquered peaks(in the order of climbing).

Input
    • On the first line, you will receive the food portions, separated by a comma and a single space (', '). 
    • On the second line, you will receive the stamina, separated by a comma and a single space (', ').

Output
    • On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
         If he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
         If he didn't manage to climb all of the peaks: "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
    • Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
"Conquered peaks:
{peak1}
{peak2}
…
{peakn}"
         If there are no concurred peaks, do NOT print this message.

    Examples:

    Input: 40, 40, 40, 40, 40, 40, 40     Output: Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
           40, 50, 60, 20, 30, 5, 2	          Conquered peaks:
						  Vihren
						  Kutelo
						  Banski Suhodol
						  Polezhan
						  Kamenitza

    Input: 10, 20, 34, 26, 12, 10, 45     Output: Alex failed! He has to organize his journey better next time -> @PIRINWINS

    02. Navy Battle
1914, September 22 – German submarine U-9 sinks three unescorted British armored cruisers HMS Aboukir, HMS Hogue, and HMS Cressy in approximately one hour. 
Imagine that they had the technology to make themselves a navigational program for the submarine and you are chosen to implement the logic.
Navigate U-9 through the battlefield, find and sink the British cruisers in the dark night, avoiding the floating mines all over the North Sea.
You will be given an integer n for the size of the battlefield (square shape). On the next n lines, you will receive the rows of the battlefield.
The submarine will start at a random position, marked with the letter 'S'.
The submarine surveys the surrounding area through its periscope, so it has to climb up to periscope depth, where it might run across naval mines.
When the submarine receives direction, it goes deep and moves one position toward the given direction.
On each turn, you will be guiding the submarine and giving it the direction, in which it should move. The commands will be "up", "down", "left" and "right".
When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
    • If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
    • If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown, the position of the mine will be marked with '-' (dash). U-9 can withstand two hits from naval mines.
The third time the submarine is hit by a mine, it disappears and the mission is failed. The battle is over and the following message should be printed on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
    • If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be marked with '-' (dash).
    • If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should be printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).
Input
    • On the first line, you are given the integer n – the size of the matrix (wall).
    • The next n lines hold the values for every row (NOT separated by anything).
    • On each of the next lines you will get a direction command.
Output
    • If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
    • If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!".
    • At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.

    Examples:

    Input: 5       Output: Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!
           *--*-           *--*-
           -S-*C           -----
           -*---           -----
           -----           -----
           -C-*C           -S-*-
           right
           down
           left
           up
           right
           right
           right
           down
           down
           down
           up
           left
           left
           left
           down

    Input: 5         Output: Mission failed, U-9 disappeared! Last known coordinates [0, 0]!
           *--*-             S----
           -S-*C             ----C
           -*---             -*---
           -----             -----
           *C-*C             *C-*C
           right
           right
           up
           left
           left
           left

    03. Student Credits
Diyan is a student and he wants your help.  
He wants a program that calculates whether he gets a diploma or not.
Write a function students_credits which receives a different number of strings. 
Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets are proportional to his points on the test.
For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test points, he will get 12.5 credits for the course.
Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's credits.
Finally, return a string on multiple lines containing:
    • Diyan's achievement message:
         If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
         Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
    • Information for each course and Diyan's credits:
    • "{course name} - {diyan's credits}"
    • Note: Each course data should be on a new line.
    • All credits must be formatted to the first decimal place.

Note: Submit only the function in the judge system
Input
    • There will be no input, just any number of strings with courses data passed to your function
Output
    • The function should return a string in the format described above:

    Examples:

    Test code: print(                                         Output: Diyan needs 198.0 credits more for a diploma.
                   students_credits(                                  Algorithms - 24.5
                       "Computer Science-12-300-250",                  Computer Science - 10.0
                       "Basic Algebra-15-400-200",                     Basic Algebra - 7.5
                       "Algorithms-25-500-490"
                   )
                )

    Test code: print(                                         Output: Diyan gets a diploma with 243.3 credits.
                   students_credits(                                  Game Engine Development - 49.0
                       "Discrete Maths-40-500-450",                    Algorithms Advanced - 45.0
                       "AI Development-20-400-400",                    Discrete Maths - 36.0
                       "Algorithms Advanced-50-700-630",               C++ Development - 24.3
                       "Python Development-15-200-200",                Mobile Development - 22.5
                       "JavaScript Development-12-500-480",            AI Development - 20.0
                       "C++ Development-30-500-405",                   QA - 20.0
                       "Game Engine Development-70-100-70",            Python Development - 15.0
                       "Mobile Development-25-250-225",                JavaScript Development - 11.5
                       "QA-20-300-300",
                    )
                )

    Test code: print(                                         Output: Diyan needs 184.2 credits more for a diploma.
                   students_credits(                                 C++ Development - 24.3
                       "Python Development-15-200-200",              Python Development - 15.0
                       "JavaScript Development-12-500-480",          JavaScript Development - 11.5
                       "C++ Development-30-500-405",                 Java Development - 5.0
                    "Java Development-10-300-150"
                   )
                )
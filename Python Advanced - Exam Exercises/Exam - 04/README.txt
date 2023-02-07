    1. Collecting Eggs
Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.
On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second line, you will receive another sequence of numbers, each representing a piece of paper with its size. 
You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.
You should comply with the following conditions:
    • If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
    • If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
        ◦ Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.
    • During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him. You should remove this egg from the sequence before it is wrapped with a piece of paper. 
        ◦ Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to Old MacDonald.
            ▪ Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.
Input
    • In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
    • In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]
Output
    • On the first line:
        ◦ If you have at least one box filled, print: 
            ▪ "Great! You filled {total count} boxes."
    • If you couldn't fill any boxes, print:
        ◦ "Sorry! You couldn't fill any boxes!"
    • On the following lines, print the eggs left or pieces of paper left if there are any:
    • Eggs left: {left eggs joined by ", "}
    • Pieces of paper left: {left pieces of paper joined by ", "}

    Examples:

    Input: 20, 13, -7, 7          Output: Great! You filled 2 boxes.
           10, 5, 20, 15, 7, 9            Pieces of paper left: 7, 5, 20, 15

    Input: 2, 4, 7, 8, 0          Output: Sorry! You couldn't fill any boxes!
           5, 6, 2                        Eggs left: 8, 0

    Input: 12, 23                 Output: Sorry! You couldn't fill any boxes!
           28, 40

2. Exit Founder

Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out. Monitor their moves closely and find out who the winner will be!
First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they are received determines the order in which they will take turns. The first player starts first.
Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
    • Only one Exit - marked with the "E" letter
    • Trap (one, many, or none) - marked with the "T" letter
    • Wall (one, many, or none) - marked with the "W" letter
    • Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving coordinates for each of the players.
They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
    • If a player hits the letter "E", he escapes the maze and wins the game.
        ◦ Print "{player} found the Exit and wins the game!" and end the program.
    • If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
        ◦ Print "{player} is out of the game! The winner is {winner}." and end the program.
    • If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
        ◦ Print "{player} hits a wall and needs to rest."
    • If a player steps on an empty position ".", nothing happens. 
    • Both players can step in the same position at the same time.

    Examples:

    Input: Tom, Jerry       Output: Tom hits a wall and needs to rest.
           . . T . . .              Jerry is out of the game! The winner is Tom.
           . . . . . .
           . . W . . .
           . . W . . E
           . . . . . .
           . T . W . .
           (3, 2)
           (1, 3)
           (5, 1)
           (5, 1)

    Input: Jerry, Tom       Output: Jerry found the Exit and wins the game!
           . T . . . W
           . . . . T .
           . W . . . T
           . T . E . .
           . . . . . T
           . . T . . .
           (1, 1)
           (3, 0)
           (3, 3)

    Input: Jerry, Tom       Output: Jerry hits a wall and needs to rest.
           . . . W . .              Tom hits a wall and needs to rest.
           . . T T . .              Tom hits a wall and needs to rest.
           . . . . . .              Jerry hits a wall and needs to rest.
           . T . W . .              Tom found the Exit and wins the game!
           W . . . E .
           . . . W . .
           (0, 3)
           (3, 3)
           (1, 3)
           (2, 2)
           (3, 5)
           (4, 0)
           (5, 3)
           (3, 1)
           (4, 4)
           (4, 4)
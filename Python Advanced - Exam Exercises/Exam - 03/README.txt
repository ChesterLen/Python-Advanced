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

02. CRUD
The abbreviation CRUD expands to Create, Read, Update and Delete.
These are the four fundamental operations in a database.

In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information. 
It consists of:
    • Letters - on one or many positions in the table
    • Numbers - on one or many positions in the table
    • Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
    • "Create, {direction}, {value}"
        ◦ The direction could be "up", "down", "left" or "right"
        ◦ If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"
        ◦ If the position is NOT empty, do NOT create a value on that position
    • "Update, {direction}, {value}"
        ◦ The direction could be "up", "down", "left" or "right"
        ◦ If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"
        ◦ If the position is empty, do NOT update the value on that position
    • "Delete, {direction}"
        ◦ The direction could be "up", "down", "left" or "right"
    • If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
    • If the position is already empty, do NOT delete it
    • "Read, {direction}"
        ◦ The direction could be "up", "down", "left" or "right"
        ◦ If you step on a letter or number, print it on the console
        ◦ If the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.
Input
    • On the first 6 lines - a matrix with positions separated by a single space
        ◦ Letters are in the range [a-zA-Z]
        ◦ Numbers are in the range [-100, 100]
    • On the next line - your first position in the format: "({row}, {column})"
    • On the following lines until you receive the command "Stop" - commands in the format shown above
Output
    • In the end, print the final matrix, each row on a new line, each position separated by a single space.

    Examples:

    Input: . . . . . .         Output: t
           . 6 . . . .                 . . . . . .
           G . S . t S                 . 6 . . . .
           . . 10 . . .                G r e a t .
           . 95 . . 8 .                . . 10 . . .
           . . P . . .                 . 95 . . 8 .
           (1, 1)                      . . P . . .
           Create, down, r
           Update, right, e
           Create, right, a
           Read, right
           Delete, right
           Stop

    Input: . . . . . .         Output: . . . . . .  
           . 6 . . . .                 . 6 . . . .
           . T . D . O                 . T . D . O 
           . . 10 A . .                . . 10 A . .
           . 95 . 80 5 .               . 95 . 80 5 . 
           . . P . t .                 . . P . t .  
           (2, 3)
           Create, down, o
           Delete, right
           Read, up
           Create, left, 20
           Update, up, P
           Stop

    Input: H 8 . . . .          Output: 8
           70 i . . . .                 i
           t . . . B .                  70
           50 . 16 . C .                H 8 . . . .
           . . . t . .                  70 i . . . .
           . 25 . . . .                 . 10 . . B .
           (0, 0)                       50 . 16 . C .
           Read, right                  . . . t . .
           Read, down                   . 25 . . . .
           Read, left
           Delete, down
           Create, right, 10
           Read, left
           Stop

    03. Song Creator
Create a function called add_songs().
It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position.
The list can consist of one, many, or no strings - each representing a line of the lyrics of the song. 
The function collects the information and concatenates the lyrics for each song (each string on a different line).
If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.
Input
    • There will be no input, just tuples passed to your function.
Output
    • Return the desired result as described above.

    Examples:

    Test code: print(add_songs(                                      Output: - Bohemian Rhapsod
                   ("Bohemian Rhapsody", []),                                - Just in Time
                   ("Just in Time",                                          Just in time, I found you just in time
                   ["Just in time, I found you just in time",                Before you came, my time was running low
                   "Before you came, my time was running low",               I was lost, the losing dice were tossed
                   "I was lost, the losing dice were tossed",                My bridges all were crossed, nowhere to go
                   "My bridges all were crossed, nowhere to go"])
                ))

    Test code: print(add_songs(                                       Output: - Beat It
                   ("Beat It", []),                                           Just beat it (beat it), beat it (beat it)
                   ("Beat It",                                                No one wants to be defeated
                   ["Just beat it (beat it), beat it (beat it)",              Showin' how funky and strong is your fight
                   "No one wants to be defeated"]),                           It doesn't matter who's wrong or right
                   ("Beat It", []),
                   ("Beat It",
                   ["Showin' how funky and strong is your fight",
                   "It doesn't matter who's wrong or right"]),
                 ))

    Test code: print(add_songs(                                        Output: - Love of my life
                   ("Love of my life",                                         Love of my life, you've hurt me
                   ["Love of my life, you've hurt me",                         You've broken my heart, and now you leave me
                   "You've broken my heart, and now you leave me",             Love of my life, can't you see?
                   "Love of my life, can't you see?",                          Bring it back, bring it back
                   "Bring it back, bring it back"]),                           Don't take it away from me
                   ("Beat It", []),                                            Because you don't know
                   ("Love of my life",                                         What it means to me
                   ["Don't take it away from me",                              - Beat It
                   "Because you don't know",                                   - Dream On
                   "What it means to me"]),                                    Every time that I look in the mirror
                   ("Dream On",
                   ["Every time that I look in the mirror"]),
                 ))
    1. Flower Finder
You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking if the following words could be found:
    • "rose"
    • "tulip"
    • "lotus"
    • "daffodil"
Start by taking the first character of the vowels collection and the last character from the consonants collection. Then check if these letters are present in one or more of the given words.
If a letter is present, that part of the word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple of letters until you find one of the given words above.
A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
    • The letter "o" is present in "rose", "lotus", and "daffodil". 
    • The letter "l" is present in "tulip", "lotus", and "daffodil".
    • The letter "f" is present in the word "daffodil" twice.
The consonant and the vowel are always removed from the collection after trying to match them with the letters in the given words (whether successful or not).
In the end, the program stops when a word is found, or there are no more vowels or consonants.
As a result, if you found a word, print it and the remaining letters in each collection in the format described below.
Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format described below.
Look at the provided examples for a better understanding of the problem.
Input
    • On the first line, you will receive vowels, separated by a single space (" ").
    • On the second line, you will receive consonants, separated by a single space (" ").
Output
    • On the first line:
        ◦ If a word is found, print it in the format: "Word found: {word_found}"
        ◦ Otherwise, print: "Cannot find any word!"
    • On the next lines, print the remaining letters in each collection (if there are any left):
        ◦ "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
        ◦ "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"

    Examples:

    Input: o e a o e a i      Output: Word found: rose
           p r s x r                  Vowels left: o e a i
				      Consonants left: p r

    Input: a a a              Output: Cannot find any word!
           x r l t p p                Consonants left: x r l

    Input: u a o i u y o e    Output: Word found: tulip
           p m t l                    Vowels left: u y o e

 2. Pawn Wars

A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H.
We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
    • Only move forward in a straight line:
            ▪ White (w) moves from the 1st rank to the 8th rank direction.
            ▪ Black (b) moves from 8th rank to the 1st rank direction.
    • Can move only 1 square at a time.
    • Can capture another pawn in from of them only diagonally:

When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on. 


Some rules apply when moving paws:
    • If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
    • If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
Input
    • On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
        ◦ Empty positions are marked with "-".
        ◦ White pawn is marked with "w"
        ◦ Black pawn is marked with "b"
Output
Print either one of the following:
    • If a pawn captures the other, print:
        ◦ "Game over! {White/Black} win, capture on {square}."
    • If a pawn reaches the last rank, print:
        ◦ "Game over! {White/Black} pawn is promoted to a queen at {square}."

    Examples:

    Input: - - - - - - b -       Output: Game over! White pawn
           - - - - - - - -               is promoted to a queen
           - - - - - - - -               at b8.
           - - - - - - - -
           - - - - - - - -
	   - w - - - - - -
	   - - - - - - - -
	   - - - - - - - -

    Input: - - - - - - - -       Output: Game over! White win,
           - - - - - - - -               capture on a3.
           - - - - - - - -
           - - - - - - - -
           - - - - - - - -
           b - - - - - - -
           - w - - - - - -
	   - - - - - - - -

03. Springtime
Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again. Farmers and gardeners plant their seeds and temperatures slowly rise.
Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). For example, dahlia="flower", shrikes="bird", dogwood="tree".
The function should sort the given spring objects in collections by their type:
    • The collections sorted by their number of elements in descending order. If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name. 
    • Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.

Input
    • There will be no input. Just parameters passed to your function.
Output
    • Return the result, sorted as described above in the format:
        ◦ "{type_one}:
	  -{spring_object_of_this_type_one}
	  -{spring_object_of_this_type_two}
	  …
	  -{spring_object_of_this_type_N}
	  {type_two}:
	  …
	  {type_N}:
	  …
	  -{last_spring_object_of_typeN}"

    Test code: example_objects = {"Water Lilly": "flower",                  Output: flower:
                                  "Swifts": "bird",                                 -Dahlia
                                  "Callery Pear": "tree",                           -Tulip
                                  "Swallows": "bird",                               -Water Lilly
                                  "Dahlia": "flower",                               bird:
                                  "Tulip": "flower",}                   	    -Swallows
                                                                                    -Swifts
                                  print(start_spring(**example_objects))            tree:
                                                                                    -Callery Pear

    Test code: example_objects = {"Swallow": "bird",                         Output: bird:
                                  "Thrushes": "bird",                                -Shrikes
                                  "Woodpeckers": "bird",                             -Swallow
                                  "Swallows": "bird",                                -Swallows
                                  "Warblers": "bird",                                -Thrushes
                                  "Shrikes": "bird",}                                -Warblers
                                                                                     -Woodpeckers

                                  print(start_spring(**example_objects))

    Tets code: example_objects = {"Magnolia": "tree",                         Output: bird:
                                  "Swallow": "bird",                                  -Shrikes
                                  "Thrushes": "bird",                                 -Swallow
                                  "Pear": "tree",                                     -Thrushes
                                  "Cherries": "tree",                                 tree:
                                  "Shrikes": "bird",                                  -Cherries
                                  "Butterfly": "insect"}                              -Magnolia
                                                                                      -Pear
                                  print(start_spring(**example_objects))              insect:
                                                                                      -Butterfly
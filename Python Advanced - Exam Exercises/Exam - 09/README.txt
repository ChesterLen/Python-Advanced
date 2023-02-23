    1. Aladdin's Gifts
Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie for help to prepare the wedding presents.
First, you will receive a sequence of integers representing the materials for every wedding present.
After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.

    Gift: Gemstone               Magic needed: 100 to 199
          Porcelain Sculpture                  200 to 299
          Golf                                 300 to 399
          Diamond Jewellery                    400 to 499

To make a present, you should take the last integer of materials and sum it with the first magic level value.
If the result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
    • If the product of the operation is under 100:
        ◦ And if it is an even number, double the materials, and triple the magic, then sum it again. 
        ◦ And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the table above.
    • If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any of the numbers in the table above.
    • If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.
Input
    • The first line of input will represent the values of materials - integers, separated by a single space
    • On the second line, you will be given the magic levels - integers, separated by a single space
Output
    • On the first line - print whether you have succeeded in crafting the presents:
    • "The wedding presents are made!"
    • "Aladdin does not have enough wedding presents."
    • On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
        ◦ "Materials left: {material1}, {material2}, …"
        ◦ "Magic left: {magicValue1}, {magicValue2}, …
    • On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"

    Input: 105 20 30 25          Output: The wedding presents are made!
           120 60 11 400 10 1            Magic left: 10, 1
					 Gemstone: 1
					 Porcelain Sculpture: 2

    Input: 30 5 21 6 0 91        Output: Aladdin does not have enough
           15 9 5 15 8                   wedding presents.
					 Materials left: 30
					 Gemstone: 1

    Input: 200                   Output: Aladdin does not have enough
           5 15 32 20 10 5               wedding presents.
					 Magic left: 15, 32, 20, 10, 5
					 Porcelain Sculpture: 1

    2. Ball in the Bucket
You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points (integers) and buckets marked with the letter "B". Rules of the game:
    • You can throw a ball only 3 times.
    • When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
    • You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
    • If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 
After the board state, you are going to receive the information for every throw on a separate line. The coordinates’ information of a hit will be in the format: "({row}, {column})".
Depending on how many points you have collected, you win one of the following:

    Football                 100 to 199 points
    Teddy Bear               200 to 299 points
    Lego Construction Set    300 or more points

Your job is to keep track of the scored points and to check if you won a prize. 

Input
    • 6 lines – matrix representing the board (each position separated by a single space)
    • On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

Output
    • On the first line:
        ◦ If you won a prize, print: 
"Good job! You scored {points} points, and you've won {prize}."
        ◦ If you did not win any prize, print the points you need to get at least the first prize: 
"Sorry! You need {points} points more to win a prize."
    1. Bombs
Ezio is still learning how to make bombs. With their help, he will save civilization. We should help Ezio to make his perfect bombs.

You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials.
Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
Bombs:
    • Datura Bombs: 40
    • Cherry Bombs: 60
    • Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
    • On the first line, you will receive the integers representing the bomb effects, separated by ", ".
    • On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
    • On the first line, print:
        ◦ if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
        ◦ if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
    • On the second line, print all bomb effects left:
        ◦ If there are no bomb effects: "Bomb Effects: empty"
        ◦ If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
    • On the third line, print all bomb casings left:
        ◦ If there are no bomb casings: "Bomb Casings: empty"
        ◦ If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
    • Then, you need to print all bombs and the count you have of them, ordered alphabetically:
        ◦ "Cherry Bombs: {count}"
        ◦ "Datura Bombs: {count}"
        ◦ "Smoke Decoy Bombs: {count}"

    Input: 5, 25, 25, 115                                       Output: You don't have enough materials to fill the bomb pouch.
           5, 15, 25, 35                                                Bomb Effects: empty
				      					Bomb Casings: empty
				      					Cherry Bombs: 0
				      					Datura Bombs: 3
				      					Smoke Decoy Bombs: 1

    Input: 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80     Output: Bene! You have successfully filled the bomb pouch!
           20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10                      Bomb Effects: 100, 80
									Bomb Casings: 20
									Cherry Bombs: 3
									Datura Bombs: 4
									Smoke Decoy Bombs: 3
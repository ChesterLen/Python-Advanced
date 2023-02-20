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
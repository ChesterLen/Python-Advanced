    1.  Ramen Shop
You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.
Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:
    • Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.
    • Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the customer.
Then try to match the same bowl of ramen (which has been decreased) with the next customer.
    • Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl.
Then try to match the same customer (which has been decreased) with the next bowl of ramen.
Look at the examples provided for a better understanding of the problem.
Input
    • On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a comma ", ".
    • On the second line, you will receive integers representing the customers, separated by a single space and a comma ", ".
Output
    • If all customers are served, print: "Great job! You served all the customers."
        ◦ Print all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of ramen left: {bowls of ramen left}"
    • Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
        ◦ Print all customers left separated by comma and space in the format "Customers left: {customers left}"

    Examples:

    Input: 14, 25, 37, 43, 19     Output: Great job! You served all the customers
	   58, 23, 37                     Bowls of ramen left: 14, 6

    Input: 30, 13, 45             Output: Out of ramen! You didn't manage to serve all customers.
           70, 25, 55, 15                 Customers left: 7, 55, 15

    Input: 30, 25                 Output: Great job! You served all the customers.
           20, 35

    2. Martian Explorer
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
    • One rover - marked with the letter "E"
    • Water deposit (one or many) - marked with the letter "W"
    • Metal deposit (one or many) - marked with the letter "M"
    • Concrete deposit (one or many) - marked with the letter "C"
    • Rock (one or many) - marked with the letter "R"
    • Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
    • When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
    • If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
    • If the rover goes out of the field, it should continue from the opposite side in the same direction.
Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
Stop the program if you run out of commands or the rover gets broken.
Input
    • On the first 6 lines, you will receive the matrix.
    • On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
    • For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete} deposit found at ({row}, {col})"
    • If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
    • If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
    • Otherwise, print on the console: "Area not suitable to start the colony."

    Examples:

    Input: - R - - - -                                             Output: Water deposit found at (3, 1)
           - - - - - R                                                     Concrete deposit found at (4, 3)
           - E - R - -             				           Metal deposit found at (5, 0)
           - W - - - -             					   Area suitable to start the colony.
           - - - C - -
	   M - - - - -
	   down, right, down, right, down, left, left, left

    Input: R - - - - -                                             Output: Water deposit found at (3, 2)
           - - C - - -                                                     Water deposit found at (4, 3)
           - - - - M -                                                     Rover got broken at (4, 5)
           - - W - - -                                                     Area not suitable to start the colony.
           - E - W - R
           - - - - - -
           up, right, down, right, right, right

    Input: R - - - - -                                             Output: Water deposit found at (4, 3)
           - - C - - -                                                     Metal deposit found at (3, 2)
           - - - - M -                                                     Concrete deposit found at (3, 0)
           C - M - R M                                                     Metal deposit found at (3, 5)
           - E - W - -                                                     Rover got broken at (3, 4)
           - - - - - -                                                     Area suitable to start the colony.
           right, right, up, left, left, left, left, left

    3. Words Sorting
Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.
Then, sort the dictionary:
    • By values in descending order, if the sum of all values of the dictionary is odd
    • By keys in ascending order, if the sum of all values of the dictionary is even
Note: Submit only the function in the judge system
Input
    • There will be no input, just any number of words passed to your function
Output
    • The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
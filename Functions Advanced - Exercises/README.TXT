    1. Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
    • On the first line, print the sum of the negatives
    • On the second line, print the sum of the positives
    • On the third line:
        ◦ If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
        ◦ If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"

	Note: you will not receive any zeroes in the input.

    Examples: 
	
    Input: 1 2 -3 -4 65 -98 12 57 -84     Output: -189
                                                   137
          					   The negatives are stronger than the positives

    Input: 1 2 3                          Output: 0
                                                  6
                                                  The positives are stronger than the negatives

    2. Keyword Arguments Length
Create a function called kwargs_length() that can receive some keyword arguments and return their length.

    Test code: dictionary = {'name': 'Peter', 'age': 25}     Output: 2
               print(kwargs_length(**dictionary))

    Test code: dictionary = {}                               Output: 0
               print(kwargs_length(**dictionary))
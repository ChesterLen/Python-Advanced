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

    3. Even or Odd
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". 
Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.

    Test code: print(even_odd(1, 2, 3, 4, 5, 6, "even"))                Output: [2, 4, 6]

    Test code: print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))    Output: [1, 3, 5, 7, 9]

    4. Numbers Filter
Create a function called even_odd_filter() that can receive a different number of named arguments. The keys will be "even" and/or "odd", and the values will be a list of numbers.  
When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you should extract only the even numbers from its list.
The function should return a dictionary sorted by the length of the lists in descending order. There will be no case of lists with the same length.

    Test code: print(even_odd_filter(                      Output: {'even': [4, 10, 2, 2],
                    odd=[1, 2, 3, 4, 10, 5],                        'odd': [1, 3, 5]}
                 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
               ))

    Test code: print(even_odd_filter(                      Output: {'odd': [5]}
                    odd=[2, 2, 30, 44, 10, 5],
               ))
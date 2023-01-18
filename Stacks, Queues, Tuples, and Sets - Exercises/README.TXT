    1. Numbers
First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
    • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
    • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
    • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
    • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
    • "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.

    Examples:

    Input: 1 2 3 4 5               Output: True
           1 2 3                           1, 2, 3, 4, 5, 6
           3                               1, 2, 3
           Add First 5 6
           Remove Second 8 9 11
           Check Subset

    Input: 5 4 2 9 9 5 4                   False
           1 1 1 5 6 5                     2, 3, 4, 5, 6, 9
           4                               6
           Add First 5 6 9 3
           Add Second 1 2 3 3 3
           Check Subset
           Remove Second 1 2 3 4 5
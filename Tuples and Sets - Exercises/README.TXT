    1. Count Same Values

You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
The number must be formatted to the first decimal point.

    Examples:
    
    Input: -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3            Output: -2.5 - 3 times
                                                              4.0 - 2 times
                                                              3.0 - 4 times
                                                              -5.5 - 1 times

    Input: 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3    Output: 2.0 - 3 times
                                                              4.0 - 6 times
                                                              5.0 - 4 times
                                                              3.0 - 7 times

    2. Students' Grades
Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.
For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.

    Examples:

    Input: 7             Output: Mark -> 5.50 2.50 3.46 (avg: 3.82)
           Peter 5.20            Peter -> 5.20 3.20 (avg: 4.20)
           Mark 5.50             Alex -> 2.00 3.00 (avg: 2.50)
           Peter 3.20
           Mark 2.50
           Alex 2.00
           Mark 3.46
           Alex 3.00

    Input: 4             Output: Ted -> 3.00 3.66 (avg: 3.33)
           Scott 4.50            Scott -> 4.50 5.00 (avg: 4.75)
           Ted 3.00
           Scott 5.00
           Ted 3.66

    Input: 5             Output: Peter -> 4.40 (avg: 4.40)
           Lee 6.00              Lee -> 6.00 5.50 6.00 (avg: 5.83)
           Lee 5.50              Kenny -> 3.30 (avg: 3.30)
           Lee 6.00
           Peter 4.40
           Kenny 3.30
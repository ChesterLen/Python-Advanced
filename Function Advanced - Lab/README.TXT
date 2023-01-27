    1. Multiplication Function
Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and returns the result of the multiplication of all of them.

    Test code:

    Input: print(multiply(1, 4, 5))             Output: 20

    Input: print(multiply(4, 5, 6, 1, 3))       Output: 360

    Input: print(multiply(2, 0, 1000, 5000))    Output: 0

    2. Person Info
Write a function called get_info that receives a name, an age, and a town and returns a string in the format: 
"This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function. Submit only the function in the judge system.

    Test code:

    Input: print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))    Output: This is George from Sofia and he is 20 years old

    3. Cheese Showcase
White a function called sorting_cheeses that receives keywords arguments:
    • The key represents the name of the cheese
    • The value is a list of quantities (integers) of the pieces of the given cheese
The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. 
If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). For each kind of cheese, return their pieces quantities in descending order.
For more clarifications, see the examples below.

    Test code:

    Input: print(                                       Output: Camembert
    sorting_cheeses(                                            500
        Parmesan=[102, 120, 135],                               430
        Camembert=[100, 100, 105, 500, 430],                    105
        Mozzarella=[50, 125],                                   100
    )                                                           100
)                                                               Parmesan
                                                                135
                                                                120
                                                                102
                                                                Mozzarella
                                                                125
                                                                50

    Input: print(                                       Output: Brie
    sorting_cheeses(                                            150
        Parmigiano=[165, 215],                                  125
        Feta=[150, 515],                                        Feta
        Brie=[150, 125]                                         515
    )                                                           150
)                                                               Parmigiano
                                                                215
                                                                165
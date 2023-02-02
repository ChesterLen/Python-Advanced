def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes = sum(x for x in args if x != 'Finish')
    for el in args:
        if el == 'Finish':
            break
        if el > volume:
            difference = el - volume
            volume -= (el - difference)
            cubes -= (el - difference)
        else:
            volume -= el
            cubes -= el
    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes} more cubes."
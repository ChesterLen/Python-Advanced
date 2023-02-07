tom_jerry = [x for x in input().split(", ")]
maze = [[x for x in input().split()] for _ in range(6)]

tom_pos = []
jerry_pos = []

tom_needs_to_wait = False
jerry_needs_to_wait = False

while True:
    first_direction = [int(x) for x in input() if x.isdigit()]
    if not tom_needs_to_wait:
        row, col = first_direction[0], first_direction[1]
        if maze[row][col] == "E":
            print(f"{tom_jerry[0]} found the Exit and wins the game!")
            break
        if maze[row][col] == "W":
            tom_needs_to_wait = True
            print(f"{tom_jerry[0]} hits a wall and needs to rest.")
        if maze[row][col] == "T":
            print(f"{tom_jerry[0]} is out of the game! The winner is {tom_jerry[1]}.")
            break
    else:
        tom_needs_to_wait = False
    
    second_direction = [int(x) for x in input() if x.isdigit()]
    if not jerry_needs_to_wait:
        row, col = second_direction[0], second_direction[1]
        if maze[row][col] == "E":
            print(f"{tom_jerry[1]} found the Exit and wins the game!")
            break
        if maze[row][col] == "W":
            jerry_needs_to_wait = True
            print(f"{tom_jerry[1]} hits a wall and needs to rest.")
        if maze[row][col] == "T":
            print(f"{tom_jerry[1]} is out of the game! The winner is {tom_jerry[0]}.")
            break
    else:
        jerry_needs_to_wait = False
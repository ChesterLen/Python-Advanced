size = 6

matrix = [[x for x in input().split()]for _ in range(size)]

first_pos = tuple(int(x) for x in input().strip("()").split(", "))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command, *data = input().split(", ")

    if command == "Stop":
        break

    r = first_pos[0] + directions[data[0]][0]
    c = first_pos[1] + directions[data[0]][1]

    first_pos = [r, c]

    if command == "Create":
        if matrix[r][c] == ".":
            matrix[r][c] = data[1]


    elif command == "Update":
        if not matrix[r][c] == ".":
            matrix[r][c] = data[1]

    elif command == "Delete":
        if not matrix[r][c] == ".":
            matrix[r][c] = "."

    elif command == "Read":
        if not matrix[r][c] == ".":
            print(matrix[r][c])

[print(*row) for row in matrix]
matrix = [input().split() for _ in range(6)]

commands = input().split(", ")

rover_pos = []

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directinos = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(len(matrix)):
    if "E" in matrix[row]:
        rover_pos = [row, matrix[row].index("E")]
        break

for command in commands:
    r = rover_pos[0] + directinos[command][0]
    c = rover_pos[1] + directinos[command][1]

    if 0 > r:
        r = 5
    elif r > len(matrix):
        r = directinos[command][0]
    if c > len(matrix):
        c = rover_pos[0]
    elif 0 > c:
        c = 5

    rover_pos = [r, c]

    if matrix[r][c] == "W":
        water_deposit += 1
        print(f"Water deposit found at {rover_pos[0], rover_pos[1]}")
    elif matrix[r][c] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at {rover_pos[0], rover_pos[1]}")
    elif matrix[r][c] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at {rover_pos[0], rover_pos[1]}")
    elif matrix[r][c] == "R":
        print(f"Rover got broken at {rover_pos[0], rover_pos[1]}")
        break

if water_deposit >= 1 and metal_deposit >= 1 and concrete_deposit >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
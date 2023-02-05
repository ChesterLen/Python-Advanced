size = int(input())
car_racing_number = input()

matrix = [[x for x in input().split()] for _ in range(size)]

car_pos = [0, 0]
final_pos = []
tunnel_pos = []

r = 0
c = 0

kilometers = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_racing_number} DNF.")
        print(f"Distance covered {kilometers} km.")
        matrix[r][c] = "C"
        [print(*row, sep="") for row in matrix]
        break
        

    r = car_pos[0] + directions[command][0]
    c = car_pos[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:

        car_pos = [r, c]

        if matrix[r][c] == "T":
            kilometers += 30
            car_pos = [r, c]
            matrix[r][c] = "."

            for row in range(size):
                if "T" in matrix[row]:
                    tunnel_pos = [row, matrix[row].index("T")]
                    car_pos = tunnel_pos
                    matrix[tunnel_pos[0]][tunnel_pos[1]] = "."
                    break

        elif matrix[r][c] == ".":
            car_pos = [r, c]
            kilometers += 10

        elif matrix[r][c] == "F":
            kilometers += 10
            matrix[r][c] = 'C'
            car_pos = [r, c]
            print(f"Racing car {car_racing_number} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            [print(*row, sep="") for row in matrix]

            while True:
                command = input()
                if command == "End":
                    break
            break
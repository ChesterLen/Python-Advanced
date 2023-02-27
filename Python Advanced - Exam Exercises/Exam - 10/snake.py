snake_territory = [list(input()) for _ in range(int(input()))]

snake_pos = []

food_quantity = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(len(snake_territory)):
    if "S" in snake_territory[row]:
        snake_pos = [row, snake_territory[row].index("S")]
        snake_territory[row][snake_pos[1]] = "."
        break

while True:
    if food_quantity >= 10:
        print("You won! You fed the snake.")
        snake_territory[snake_pos[0]][snake_pos[1]] = "S"
        break

    command = input()

    r = snake_pos[0] + directions[command][0]
    c = snake_pos[1] + directions[command][1]

    if not (0 <= r < len(snake_territory) and 0 <= c < len(snake_territory)):
        print("Game over!")
        break

    if snake_territory[r][c] == "*":
        food_quantity += 1
        snake_territory[r][c] = "."
    if snake_territory[r][c] == "B":
        snake_territory[r][c] = "."
        for row in range(len(snake_territory)):
            if "B" in snake_territory[row]:
                snake_pos = [row, snake_territory[row].index("B")]
                snake_territory[row][snake_pos[1]] = "."
        continue
    else:
        snake_territory[r][c] = "."
    snake_pos = [r, c]

print(f"Food eaten: {food_quantity}")
[print(*row, sep="") for row in snake_territory]
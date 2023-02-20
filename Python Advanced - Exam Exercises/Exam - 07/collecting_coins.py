field = [input().split() for _ in range(int(input()))]

collected_coins = 0

player_pos = []
player_path = []

for row in range(len(field)):
    if "P" in field[row]:
        player_pos = [row, field[row].index("P")]
        player_path.append([row, player_pos[1]])
        break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break

    command = input()

    r = player_pos[0] + directions[command][0]
    c = player_pos[1] + directions[command][1]

    if r > len(field) - 1:
        r = 0
    elif r < 0:
        r = len(field) - 1
    if c > len(field) - 1:
        c = 0
    elif c < 0:
        c = len(field) - 1
    
    player_pos = [r, c]

    if [r, c] in player_path:
        player_path.append([r, c])
        continue
    if field[r][c] == "X":
        player_path.append([r, c])
        collected_coins = round(collected_coins - (collected_coins * 50 / 100))
        print(f"Game over! You've collected {collected_coins} coins.")
        break
    elif field[r][c].isdigit():
        collected_coins += int(field[r][c])

    player_path.append([r, c])

print("Your path:")
for step in player_path:
    print(step)
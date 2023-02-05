size = int(input())
battlefield = [[x for x in input()] for _ in range(size)]

cruiser_destroyed = 0
u_9_submarines_hits = 0

u_9_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    if "S" in battlefield[row]:
        u_9_pos = [row, battlefield[row].index("S")]
        battlefield[row][u_9_pos[1]] = "-"

while True:
    command = input()
    r = u_9_pos[0] + directions[command][0]
    c = u_9_pos[1] + directions[command][1]

    u_9_pos = [r, c]

    if battlefield[r][c] == "C":
        cruiser_destroyed += 1
        battlefield[r][c] == "-"
        if cruiser_destroyed == 3:
            battlefield[r][c] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    elif battlefield[r][c] == "*":
        u_9_submarines_hits += 1
        battlefield[r][c] == "-"
        if u_9_submarines_hits == 3:
            battlefield[r][c] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            break

    battlefield[r][c] = "-"

[print(*row, sep="") for row in battlefield]
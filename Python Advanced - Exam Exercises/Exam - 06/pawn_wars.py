borad = [input().split() for _ in range(8)]

white_pos = []
black_pos = []

for row in range(8):
    if "w" in borad[row]:
        white_pos = [row, borad[row].index("w")]
    if "b" in borad[row]:
        black_pos = [row, borad[row].index("b")]

going_up = 8 - white_pos[0]
going_down = 8 - black_pos[0]

while True:
    r_up = white_pos[0]
    c_up = white_pos[1]

    borad[r_up][c_up] = "-"

    if going_up == 8:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_pos[1])}{going_up}.")
        break
    
    if borad[r_up-1][c_up-1] == "b":
        white_pos = [r_up-1, c_up-1]
        borad[white_pos[0]][white_pos[1]] = "w"
        print(f"Game over! White win, capture on {chr(97 + white_pos[1])}{8 - white_pos[0]}.")
        break

    if borad[r_up-1][c_up+1] == "b":
        white_pos = [r_up-1, c_up+1]
        borad[white_pos[0]][white_pos[1]] = "w"
        print(f"Game over! White win, capture on {chr(97 + white_pos[1])}{8 - white_pos[0]}.")
        break

    r_up = white_pos[0] - 1
    c_up = white_pos[1]

    white_pos = [r_up, c_up]
    borad[r_up][c_up] = "w"
    going_up += 1


    r_down = black_pos[0]
    c_down = black_pos[1]

    borad[r_down][c_down] = "-"

    if going_down == 1:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_pos[1])}{going_down}.")
        break

    if borad[r_down+1][c_down+1] == "w":
        black_pos = [r_down+1, c_down+1]
        borad[black_pos[0]][black_pos[1]] = "b"
        print(f"Game over! Black win, capture on {chr(97 + black_pos[1])}{8 - black_pos[0]}.")
        break

    if borad[r_down+1][c_down-1] == "w":
        black_pos = [r_down+1, c_down-1]
        borad[black_pos[0]][black_pos[1]] = "b"
        print(f"Game over! Black win, capture on {chr(97 + black_pos[1])}{8 - black_pos[0]}.")
        break

    r_down = black_pos[0] + 1
    c_down = black_pos[1]

    black_pos = [r_down, c_down]
    borad[r_down][c_down] = "b"
    going_down -= 1
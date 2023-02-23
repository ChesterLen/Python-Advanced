board = [input().split() for _ in range(6)]

throw_limit = 3
total_points = 0

hit_positions = []

while True:
    if throw_limit == 0:
        break
    
    throw = [int(x) for x in input().strip("()").split(", ") if x.isdigit()]
    
    r = throw[0]
    c = throw[1]

    if not (0 <= r < 6 and 0 <= c < 6):
        throw_limit -= 1
        continue

    if board[r][c] == "B":
        if [r, c] not in hit_positions:
            hit_positions.append([r, c])
            for row in range(6):
                if board[row][c].isdigit():
                    total_points += int(board[row][c])
    
    throw_limit -= 1

if 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif 300 <= total_points:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
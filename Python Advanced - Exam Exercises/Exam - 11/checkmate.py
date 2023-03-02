def queens(queen_position, coordinates_):
    for coordinate in coordinates_:
        r = queen_position[0] + coordinate[0]
        c = queen_position[1] + coordinate[1]

        while 0 <= r < 8 and 0 <= c < 8:
            if matrix[r][c] == "Q":
                break
            elif matrix[r][c] == "K":
                return [r, c]
            
            r += coordinate[0]
            c += coordinate[1]


matrix = [input().split() for _ in range(8)]
matrix_copy = [row.copy() for row in matrix]
queen_positions_list = []
queens_capturers = []

coordinates = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)

for row in range(8):
    for pos in matrix_copy[row]:
        if pos == "Q":
            queen_pos = [row, matrix_copy[row].index("Q")]
            queen_positions_list.append(queen_pos)
            matrix_copy[row][queen_pos[1]] = "."

for queen in queen_positions_list:
    queen_capturer = queens(queen, coordinates)
    if queen_capturer:
        queens_capturers.append(queen)

if queens_capturers:
    print(*queens_capturers, sep="\n")
else:
    print("The king is safe!")
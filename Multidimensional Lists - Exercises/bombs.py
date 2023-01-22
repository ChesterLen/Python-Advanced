n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),   # left
    (0, 1),  # right
    (-1, 1),  # top-right
    (-1, -1),  # top-left
    (1, -1),  # dawn-left
    (1, 1),  # dawn_right
    (0, 0),  # current-position
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*matrix[r], sep=" ") for r in range(n)]

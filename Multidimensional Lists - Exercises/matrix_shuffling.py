def check_valid_index(indices):
    if set(indices[:2]).issubset(valid_rows) and set(indices[2:]).issubset(valid_cols):
        return True

    return False


def swap_command(command_, indices):
    if check_valid_index(indices) and command_ == "swap" and len(indices) == 4:
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[" ".join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(columns)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_command(command, info)

matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row_data = input()
    matrix.append(row_data)

symbol = input()

for _ in matrix:
    if symbol in _:
        print(f"{(matrix.index(_), _.index(symbol))}")
        break
else:
    print(f"{symbol} does not occur in the matrix")

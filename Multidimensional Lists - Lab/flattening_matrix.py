matrix_rows = int(input())

matrix = []
flattening_matrix = []

for _ in range(matrix_rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

for i in matrix:
    for j in i:
        flattening_matrix.append(j)

print(flattening_matrix)

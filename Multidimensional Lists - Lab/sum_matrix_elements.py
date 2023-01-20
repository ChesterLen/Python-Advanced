matrix_size = [int(x) for x in input().split(", ")]
row, column = matrix_size

matrix = []
matrix_sum = 0

for i in range(row):
    row_data = list(map(int, input().split(", ")))
    matrix.append(row_data)
    matrix_sum += sum(row_data)

print(matrix_sum)
print(matrix)

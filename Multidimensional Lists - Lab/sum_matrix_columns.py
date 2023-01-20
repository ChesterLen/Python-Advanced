matrix_size = [int(x) for x in input().split(", ")]
rows, columns = matrix_size

matrix = []
total_sum = 0

for i in range(rows):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)

for i in range(columns):
    for j in matrix:
        total_sum += j[i]
    print(total_sum)
    total_sum = 0

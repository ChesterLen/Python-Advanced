matrix_size = int(input())

matrix = []
total_sum = 0

for _ in range(matrix_size):
    rows_data = list(map(int, input().split()))
    matrix.append(rows_data)
    total_sum += matrix[_][_]

print(total_sum)

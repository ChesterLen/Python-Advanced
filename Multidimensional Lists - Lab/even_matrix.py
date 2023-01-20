matrix_rows = int(input())

matrix = []

for _ in range(matrix_rows):
    even_numbers = list(map(int, input().split(", ")))
    matrix.append([x for x in even_numbers if x % 2 == 0])

print(matrix)

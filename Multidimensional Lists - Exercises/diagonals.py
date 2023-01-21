matrix = [[int(x) for x in input().split(", ")] for i in range(int(input()))]

total_sum = 0
total_sum_2 = 0

diagonal_1 = []
diagonal_2 = []

for i in range(len(matrix)):
    diagonal_1.append(matrix[i][i])
    total_sum += matrix[i][i]
    diagonal_2.append(matrix[i][-(i + 1)])
    total_sum_2 += matrix[i][-(i + 1)]

print(f"Primary diagonal: {', '.join(str(x) for x in diagonal_1)}. Sum: {total_sum}\n\
Secondary diagonal: {', '.join(str(x) for x in diagonal_2)}. Sum: {total_sum_2}")

line = input().split("|")

sub_matrix = []

for substring in line[::-1]:
    sub_matrix.extend(substring.split())

print(*sub_matrix)

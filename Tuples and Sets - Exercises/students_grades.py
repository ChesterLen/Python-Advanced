lines_count = int(input())
students_data = {}

for _ in range(lines_count):
    students_name, grade = input().split()
    if students_name not in students_data.keys():
        students_data[students_name] = []
    students_data[students_name].append(float(grade))

for item, value in students_data.items():
    convert_values_to_string = " ".join(map(lambda grade_: f"{grade_:.2f}", value))
    average_grade = sum(value) / len(value)
    print(f"{item} -> {convert_values_to_string} (avg: {average_grade:.2f})")

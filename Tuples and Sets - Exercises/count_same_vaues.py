values = tuple(map(float, input().split()))
counter_of_values = {value: values.count(value) for value in values}
values_counter = {}

for value in values:
    if value not in values_counter:
        values_counter[value] = 0
    values_counter[value] += 1

for item, value in values_counter.items():
    print(f"{item:.1f} - {value} times")

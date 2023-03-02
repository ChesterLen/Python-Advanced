tasks = [int(x) for x in input().split(', ')]
wanted_job_index = int(input())
dictionary = {}
clock_cycles = 0

for i in range(len(tasks)):
    current_task = tasks[i]
    dictionary[i] = current_task

sorted_dict = dict(sorted(dictionary.items(), key= lambda x: (x[1],[0])))

for x in sorted_dict.keys():
    clock_cycles += sorted_dict[x]
    if x == wanted_job_index:
        break

print(clock_cycles)
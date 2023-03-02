from collections import deque

def best_list_pureness(*args):
    rotations = args[1]
    max_purensess_rotation = 0
    deque_1 = deque(args[0])
    max_purensess = -1

    for rotation in range(rotations + 1):
        deque_1_sum = 0
        for num in deque_1:
            deque_1_sum += num * deque_1.index(num)
        deque_1.rotate(1)

        if max_purensess < deque_1_sum:
            max_purensess_rotation = rotation
            max_purensess = deque_1_sum
      
    return f"Best pureness {max_purensess} after {max_purensess_rotation} rotations"
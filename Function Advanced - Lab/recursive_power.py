def recursive_power(num, power):
    if num == 1:
        return 1
    if power == 1:
        return num

    return num * recursive_power(num, power - 1)

def even_odd(*args):
    list_args = list(args)
    command = list_args.pop()

    if command == "even":
        return list(num for num in list_args if num % 2 == 0)
    return list(num for num in list_args if num % 2 != 0)


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

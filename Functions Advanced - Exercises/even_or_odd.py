def even_odd(*args):
    list_args = list(args)
    command = list_args.pop()

    if command == "even":
        return list(num for num in list_args if num % 2 == 0)
    return list(num for num in list_args if num % 2 != 0)

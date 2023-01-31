def func_executor(*functions_data):
    result = []

    for func, args in functions_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return "\n".join(result)

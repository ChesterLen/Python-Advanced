def start_spring(**kwargs):
    result_string = ""
    sorted_kwargs = {}
    new_kwargs = {}
    for key, value in kwargs.items():
        if value not in new_kwargs.keys():
            new_kwargs[value] = []
        new_kwargs[value].append(key)
    
    sorted_kwargs = sorted(new_kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for item in sorted_kwargs:
        result_string += f"{item[0]}:\n"
        for value in sorted(item[1]):
            result_string += f"-{value}\n"

    return result_string
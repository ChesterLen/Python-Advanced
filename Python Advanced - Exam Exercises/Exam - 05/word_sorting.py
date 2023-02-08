def words_sorting(*args):
    words_values_dict = {}
    words_values_dict_sorted_as_string = ""

    sum_ascii_values = 0

    for word in args:
        if word not in words_values_dict.keys():
            words_values_dict[word] = 0
        for char in word:
            words_values_dict[word] += ord(char)

    sum_ascii_values = sum(words_values_dict.values())

    if sum_ascii_values % 2 != 0:
        sorted_dict_by_values =  dict(sorted(words_values_dict.items(), key=lambda x: -x[1]))

        for item, value in sorted_dict_by_values.items():
            words_values_dict_sorted_as_string += f"{item} - {value}\n"
    else:
        sorted_dict_by_values = dict(sorted(words_values_dict.items(), key=lambda x: x[0]))

        for item, value in sorted_dict_by_values.items():
            words_values_dict_sorted_as_string += f"{item} - {value}\n"
    
    return words_values_dict_sorted_as_string


print(
    words_sorting(
        'cacophony',         
        'accolade'
  ))
def positives(numbers_):
    for x in numbers_:
        if x > 0:
            positives_list.append(x)
    return numbers_


def negatives(numbers_):
    for x in numbers_:
        if x < 0:
            negatives_list.append(x)
    return negatives_list


def print_():
    if sum(positives_list) > abs(sum(negatives_list)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


positives_list = []
negatives_list = []

numbers = [int(x) for x in input().split()]

positives(numbers)
negatives(numbers)

print(sum(negatives_list))
print(sum(positives_list))

print_()

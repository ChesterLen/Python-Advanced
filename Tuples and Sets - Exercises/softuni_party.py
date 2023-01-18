def function_sort_by_vip(was_absent_guests):
    print(len(was_absent_guests))

    for guest in sorted(was_absent_guests):
        print(guest)


def data_for_arrived_guests():
    arrived_guests_list_ = []

    while True:
        guest = input()
        if guest == "END":
            break
        else:
            arrived_guests_list_.append(guest)

    return arrived_guests_list_


guests_count = int(input())
guests_list = [input() for _ in range(guests_count)]
arrived_guests_list = data_for_arrived_guests()
was_absent_guests_set = set(guests_list).difference(arrived_guests_list)
function_sort_by_vip(was_absent_guests_set)

def flights(*args):
    flights_dict = {}

    for flight in range(0, len(args) + 1, 2):
        if args[flight] == "Finish":
            break
        if args[flight] not in flights_dict.keys():
            flights_dict[args[flight]] = 0
        flights_dict[args[flight]] += args[flight + 1]
    
    return flights_dict

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
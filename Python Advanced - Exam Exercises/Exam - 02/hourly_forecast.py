def forecast(*args):
    locations = {}
    sunny = ""
    cloudy = ""
    rainy = ""

    for k, v in args:
        if k not in locations.keys():
            locations[k] = ""
        locations[k] = v

    sorted_dict = {k: v for k, v in sorted(locations.items(), key=lambda x: (x[1], x[0]))}

    for item, value in sorted_dict.items():
        if value == "Sunny":
            sunny += f"{item} - {value}\n"
        
        elif value == "Cloudy":
            cloudy += f"{item} - {value}\n"

        elif value == "Rainy":
            rainy += f"{item} - {value}\n"
    
    return sunny + cloudy + rainy
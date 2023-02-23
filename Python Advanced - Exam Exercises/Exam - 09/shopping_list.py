def shopping_list(budget, **kwargs):
    products = [item for item in kwargs.keys()]
    products_types = set()
    result = ""
    if budget >= 100:
        for item, value in kwargs.items():
            if budget >= value[0] * value[1]:
                budget -= value[0] * value[1]
                products_types.add(item)
                products.pop(products.index(item))
                result += f"You bought {item} for {value[0] * value[1]:.2f} leva.\n"
            if len(products_types) == 5:
                break
            elif not products:
                break
        return result
    
    return "You do not have enough budget."
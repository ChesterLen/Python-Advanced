def stock_availability(list_boxes, *args):
    if args[0] == "delivery":
        for box in args[1:]:
            list_boxes.append(box)
    elif args[0] == "sell":
        if len(args) > 1:
            if type(args[1]) == int:
                for box in range(args[1]):
                    list_boxes.remove(list_boxes[0])
            else:
                for box in list_boxes:
                    if box in args:
                        list_boxes = set(list_boxes).difference(set(args))
        else:
            list_boxes.remove(list_boxes[0])
    
    return list(list_boxes)
   


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
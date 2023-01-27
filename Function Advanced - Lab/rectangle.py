def rectangle(length, width):
    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return (length * 2) + (width * 2)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"Rectangle area: {rectangle_area()}\nRectangle perimeter: {rectangle_perimeter()}"

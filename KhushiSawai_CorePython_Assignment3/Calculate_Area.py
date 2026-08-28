# Create functions to calculate the area of basic shapes
def circle():
    r = int(input("Enter radius:"))
    Areac = 3.14 * r * r
    print(f"Area of circle: {Areac}")
def rectangle():
    length = int(input("Enter length:"))
    width = int(input("Enter width:"))
    rec = length * width
    print(f"Area of rectangle: {rec}")
def square():
    side = int(input("Enter side:"))
    side = int(input("Enter side:"))
    square = side * side
    print(f"Area of square: {square}")
# Call the function
circle()
rectangle()
square()

    
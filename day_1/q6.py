#q6
def calculate_circle_properties():
    pi=3.14
    radius = float(input("Enter the radius of the circle: "))
    area = pi * radius * radius
    circumference = 2 * pi * radius
    print("The area of the circle is:", area)
    print("The circumference of the circle is:", circumference)
    calculate_circle_properties()
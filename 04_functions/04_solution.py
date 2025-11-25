import math

def circle_calculations(radius):
    pi = math.pi
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference


r = float(input("Enter the radius of the circle: "))
a,c = circle_calculations(r)

print("The area and circumference of the circle with radius", r, "are: area=", round(a,2), "circumference=", round(c,2))


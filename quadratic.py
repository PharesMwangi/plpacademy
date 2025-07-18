import math


a, b, c = map(float, input("Enter three float values (a, b, c) separated by space: ").split())

d = b*b - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d))/ (2*a)
    x2 = (+b + math.sqrt(d))/ (2*a)
    print("Distinct roots:", x1, x2)

elif d == 0:
    x = -b/ (2*a)
    print("Double roots:", x)

else :
    real = -b /(2*a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("Complex roots:", real, "+", imaginary, "i", "and", real, "-", imaginary, "i")

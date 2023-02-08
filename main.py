import math

a = input("A: ")
b = input("B: ")
c = input("C: ")

delta = b ** 2 - (4 * a * c)
primary = -b + (math.sqrt(delta))
secondary = -b - (math.sqrt(delta))
result1 = primary / (2 * a)
result2 = secondary / (2 * a)

print(f"x1 = {result1}")
print(f"x2 = {result2}")
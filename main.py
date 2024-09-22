import math
x = int(input("Введите x:"))
y = int(input("Введите y:"))
g = abs(x ** (y / x) - (y / x) ** (1 / 3)) + (y - x)
print (f"g = {g}")
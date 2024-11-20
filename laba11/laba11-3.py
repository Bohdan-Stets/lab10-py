import math

def trigonometric_expression(n, x):
    if n == 1:
        return math.sin(x) * math.cos(x)
    elif n == 2:
        return math.sin(x**2) + math.cos(x)
    else:
        return 1 - math.sin(x)

n = int(input("Введіть значення n: "))
x = float(input("Введіть значення x (у радіанах): "))

result = trigonometric_expression(n, x)
print("Результат:", result)

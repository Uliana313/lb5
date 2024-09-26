import math

D = float(input("Введіть діаметр кулі: "))

x = float(input("Введіть координату x: "))
y = float(input("Введіть координату y: "))
z = float(input("Введіть координату z: "))

radius = D / 2

distance = math.sqrt(x**2 + y**2 + z**2)

if distance <= radius:
    print("Точка належить кулі.")
else:
    print("Точка не належить кулі.")

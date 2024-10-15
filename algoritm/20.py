import math
R = float(input("Внешний(R): "))
r = float(input("Внутренний(r): "))
if R <= r:
    print("Ошибка: Внешний радиус должен быть больше внутреннего.")
else:
    area = math.pi * (R ** 2 - r ** 2)
    print(f"Площадь кольца: {area:.2f}")
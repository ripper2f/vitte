x1, y1 = map(float, input("Введите координаты первой точки (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты третьей точки (x3 y3): ").split())

side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
side3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Треугольник может существовать.")

    if side1 == side2 == side3:
        triangle_type = "равносторонний"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "произвольный"

    sides_sorted = sorted([side1, side2, side3])
    if abs(sides_sorted[0] ** 2 + sides_sorted[1] ** 2 - sides_sorted[2] ** 2) < 1e-9:
        triangle_type += ", прямоугольный"

    print("Вид треугольника:", triangle_type)

    semi_perimeter = (side1 + side2 + side3) / 2
    area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

    perimeter = side1 + side2 + side3

    print("Площадь треугольника:", area)
    print("Периметр треугольника:", perimeter)
else:
    print("Треугольник не может существовать.")

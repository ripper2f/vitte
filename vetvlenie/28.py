x1, y1 = map(float, input("Введите координаты точки A (x1, y1): ").split())
x2, y2 = map(float, input("Введите координаты точки B (x2, y2): ").split())
x3, y3 = map(float, input("Введите координаты точки C (x3, y3): ").split())

def triangle_area(xa, ya, xb, yb, xc, yc):
    return abs((xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2.0)

area_ABC = triangle_area(x1, y1, x2, y2, x3, y3)

area_OAB = triangle_area(0, 0, x1, y1, x2, y2)
area_OAC = triangle_area(0, 0, x1, y1, x3, y3)
area_OBC = triangle_area(0, 0, x2, y2, x3, y3)

if area_ABC == area_OAB + area_OAC + area_OBC:
    print("Начало координат находится внутри треугольника ABC")
else:
    print("Начало координат находится вне треугольника ABC")

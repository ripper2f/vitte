a = float(input("Введите длину ребра a: "))
b = float(input("Введите длину ребра b: "))
c = float(input("Введите длину ребра c: "))
x = float(input("Введите ширину отверстия x: "))
y = float(input("Введите высоту отверстия y: "))

if ((a <= x and b <= y) or (a <= y and b <= x) or
    (a <= x and c <= y) or (a <= y and c <= x) or
    (b <= x and c <= y) or (b <= y and c <= x)):
    print("Кирпич пройдет через отверстие")
else:
    print("Кирпич не пройдет через отверстие")

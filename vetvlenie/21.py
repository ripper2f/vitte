x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if x > 0 and y > 0:
    print("Точка находится в первой четверти.")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти.")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти.")
elif x > 0 and y < 0:
    print("Точка находится в четвертой четверти.")
elif x == 0 and y == 0:
    print("Точка находится в начале координат.")
elif x == 0:
    print("Точка находится на оси y.")
elif y == 0:
    print("Точка находится на оси x.")

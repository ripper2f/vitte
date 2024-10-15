X, Y, Z = input("Введите три цифры через пробел: ").split()

number = int(X + Y + Z)

if number % 10 < 5:
    nearest = number - (number % 10)
else:
    nearest = number + (10 - (number % 10))

print("Ближайшее к числу", number, "число, кратное 10:", nearest)

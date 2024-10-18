a = 0

while True:
    b = int(input("Введите число (0 для выхода): "))

    if b == 0:
        break
    a += b

print("Сумма введенных чисел:", a)

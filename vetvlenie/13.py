n = int(input("Введите натуральное число от 0 до 1000: "))

if 0 <= n <= 1000:
    count = 0
    if n == 0:
        count = 1
    else:
        while n > 0:
            n //= 10
            count += 1
    print("Количество знаков:", count)
else:
    print("Число вне диапазона!")

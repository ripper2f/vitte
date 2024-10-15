a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    result = a + b
    print(f"Результат: {result}")
elif operation == '-':
    result = a - b
    print(f"Результат: {result}")
elif operation == '*':
    result = a * b
    print(f"Результат: {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"Результат: {result}")
    else:
        print("Ошибка: Деление на ноль!")
else:
    print("Ошибка: Неверная операция!")

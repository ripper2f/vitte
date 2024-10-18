max_num = 0
second_max = 0

while True:
    num = int(input("Введите натуральное число (0 для завершения): "))

    if num == 0:
        break

    if num > max_num:
        second_max = max_num
        max_num = num
    elif num > second_max and num < max_num:
        second_max = num

if second_max == 0:
    print("Нет второго по величине элемента.")
else:
    print("Второй по величине элемент:", second_max)

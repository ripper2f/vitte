K = int(input("Введите число K (от 1 до 99): "))

if K < 1 or K > 99:
    print("Введите число в пределах от 1 до 99.")
else:
    if K % 10 == 1 and K % 100 != 11:
        suffix = "год"
    elif K % 10 in [2, 3, 4] and not (12 <= K % 100 <= 14):
        suffix = "года"
    else:
        suffix = "лет"

    print(f"Мне {K} {suffix}")
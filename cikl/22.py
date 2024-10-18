n = int(input("Введите число: "))

if n <= 1:
    print(f"{n} не является простым числом.")
else:
    is_prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} является простым числом.")
    else:
        print(f"{n} не является простым числом.")

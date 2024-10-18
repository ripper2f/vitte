n = int(input("Введите число n: "))

largest_prime = None

for num in range(n - 1, 1, -1):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        largest_prime = num
        break

if largest_prime is not None:
    print(f"Самое большое простое число меньше {n} - это {largest_prime}.")
else:
    print(f"Нет простых чисел меньше {n}.")

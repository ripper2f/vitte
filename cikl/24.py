n = int(input("Введите значение n: "))

for c in range(1, n + 1):
    for a in range(1, c + 1):
        for b in range(1, c + 1):
            if a**2 + b**2 == c**2:
                print(f"a = {a}, b = {b}, c = {c}")
n = int(input("Введите n: "))
k = int(input("Введите k: "))

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a + b == k:
            print(f"({a}, {b})")
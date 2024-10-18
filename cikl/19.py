A = int(input("Введите натуральное число A (> 1): "))
if A <= 1:
    print(-1)
else:
    n1, n2 = 1, 1
    n = 2

    while n2 < A:
        n1, n2 = n2, n1 + n2
        n += 1

    if n2 == A:
        print(n)
    else:
        print(-1)
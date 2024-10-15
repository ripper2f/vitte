a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))

if a <= b <= c <= d:
    max_value = max(a, b, c, d)
    a = b = c = d = max_value
elif a > b > c > d:
    pass  # Числа остаются без изменения
else:
    a = a**2
    b = b**2
    c = c**2
    d = d**2

print("Результаты:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

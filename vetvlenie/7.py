l = float(input("Длина: "))
r = float(input("Радиус: "))

if r * 2 <= l:
    print("Круг может быть вписан в квадрат")
elif l <= r * (2 ** 0.5):
    print("Квадрат может быть вписан в круг")
else:
    print("Ни одно из утверждений не выполнено")
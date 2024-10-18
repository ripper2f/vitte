num = int(input("Введите десятичное число: "))

binary = ""
n = num

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

ternary = ""
n = num

while n > 0:
    ternary = str(n % 3) + ternary
    n = n // 3

base15 = ""
n = num

while n > 0:
    remainder = n % 15
    if remainder < 10:
        base15 = str(remainder) + base15
    else:
        base15 = chr(remainder - 10 + ord('A')) + base15
    n = n // 15

print("Двоичная запись:", binary)
print("Троичная запись:", ternary)
print("Пятнадцатеричная запись:", base15)
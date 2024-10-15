number = int(input("Введите четырехзначное число: "))

digits = []
for i in range(4):
    digits.append(number % 10)
    number //= 10

count = 0

for i in range(10):
    if digits.count(i) == 2:
        count += 1

if count == 1:
    print("True")
else:
    print("False")

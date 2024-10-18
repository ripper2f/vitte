n = int(input("Введите количество чисел: "))

sum_arithmetic = 0
product_geometric = 1
count = 0

for i in range(n):
    number = float(input(f"Введите число {i + 1}: "))
    sum_arithmetic += number
    product_geometric *= number
    count += 1

if count > 0:
    average_arithmetic = sum_arithmetic / count
    average_geometric = product_geometric ** (1 / count)
else:
    average_arithmetic = 0
    average_geometric = 0

print(f"Среднее арифметическое: {average_arithmetic}")
print(f"Среднее геометрическое: {average_geometric}")

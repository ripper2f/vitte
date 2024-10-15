D = int(input("Введите число (D): "))
M = int(input("Введите номер месяца (M): "))
Y = int(input("Введите год (Y): "))

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_year = D
for i in range(M - 1):
    day_of_year += days_in_months[i]
print("Номер дня в году:", day_of_year)

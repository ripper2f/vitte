x = float(input("Введите пробег в первый день (в километрах): "))
target = float(input("Введите целевой пробег (в километрах): "))

day = 1
current_distance = x

while current_distance < target:
    day += 1
    current_distance += current_distance * 0.10

print("На", day, "день пробег спортсмена составит не менее", target, "километров.")

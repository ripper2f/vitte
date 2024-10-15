N = int(input("Введите длину бассейна (N): "))
M = int(input("Введите ширину бассейна (M): "))

x = int(input("Введите расстояние от пловца до одного из длинных бортиков (x): "))
y = int(input("Введите расстояние от пловца до одного из коротких бортиков (y): "))

distance_to_long_edge = min(x, N - x)
distance_to_short_edge = min(y, M - y)

min_distance = min(distance_to_long_edge, distance_to_short_edge)

print("Минимальное расстояние до бортика бассейна:", min_distance)

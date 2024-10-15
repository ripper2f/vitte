min_x = 1
max_x = 3
step = 0.5

x = min_x

print(" x      |       y")
print("---------------------")

while x <= max_x:
    y = -0.23 * x * x + x
    print(f"{x:.2f}   |   {y:.2f}")
    x += step
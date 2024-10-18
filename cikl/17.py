count = 0
previous = None

while True:
    number = int(input())
    if number == 0:
        break

    if previous is not None and number > previous:
        count += 1

    previous = number

print(count)

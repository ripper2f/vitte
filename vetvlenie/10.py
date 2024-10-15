K = int(input("Введите количество грибов: "))

if K % 10 == 1 and K % 100 != 11:
    ending = "гриб"
elif K % 10 in [2, 3, 4] and not (K % 100 in [12, 13, 14]):
    ending = "гриба"
else:
    ending = "грибов"

print(f"Мы нашли в лесу {K} {ending}.")
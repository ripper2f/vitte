a = int(input())
m31 = [1, 3, 5, 7, 8, 10, 11]
m30 = [4, 6, 9, 12]
m28 = [2]
if a in m31:
    print(f"В {a} месяце 31 день")
elif a in m30:
    print(f"В {a} месяце 30 дней")
elif a in m28:
    print(f"В {a} месяце 28 дней")
else:
    print("каво")
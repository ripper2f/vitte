s = int(input())
h = s // 3600
ost = s % 3600
m = ost // 60
print(f"{h} час {'1 минута' if m == 1 else f'{m} минут'}")
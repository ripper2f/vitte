i1 = int(input("Иванов 1 тур:"))
i2 = int(input("Иванов 2 тур:"))
i3 = int(input("Иванов 3 тур:"))
p1 = int(input("Петров 1 тур:"))
p2 = int(input("Петров 2 тур:"))
p3 = int(input("Петров 3 тур:"))
s1 = int(input("Сидоров 1 тур:"))
s2 = int(input("Сидоров 2 тур:"))
s3 = int(input("Сидоров 3 тур:"))

i = i1+i2+i3
print(f"Иванов набрал за все туры: {i}")
p = p1+p2+p3
print(f"Петров набрал за все туры: {p}")
s = s1+s2+s3
print(f"Сидоров набрал за все туры: {s}")

tur1 = max(i1, p1, s1)
if i1 is tur1:
    print(f"Первый тур победил Иванов, набрав: {i1} баллa")
elif p1 is tur1:
    print(f"Первый тур победил Петров, набрав: {p1} баллa")
elif s1 is tur1:
    print(f"Первый тур победил Сидоров, набрав: {s1} баллa")
tur2 = max(i2, p2, s2)
if i2 is tur2:
    print(f"Второй тур победил Иванов, набрав: {i2} баллa")
elif p2 is tur2:
    print(f"Второй тур победил Петров, набрав: {p2} баллa")
elif s2 is tur2:
    print(f"Второй тур победил Сидоров, набрав: {s2} баллa")
tur3 = max(i3, p3, s3)
if i3 is tur3:
    print(f"Третий тур победил Иванов, набрав: {i3} баллa")
elif p3 is tur3:
    print(f"Третий тур победил Петров, набрав: {p3} баллa")
elif s3 is tur3:
    print(f"Третий тур победил Сидоров, набрав: {s3} баллa")

if i > p and i > s:
    print("Победил Иванов")
elif i == p:
    print("Победил Иванов и Петров")
elif i == s:
    print("Победил Иванов и Сидоров")
if p > i and p > s:
    print("Победил Петров")
elif p == i:
    print("Победил Петров и Иванов")
elif p == s:
    print("Победил Петров и Сидоров")
if s > i and s > p:
    print("Победил Сидоров")
elif s == i:
    print("Победил Сидоров и Иванов")
elif s == p:
    print("Победил Сидоров и Петров")
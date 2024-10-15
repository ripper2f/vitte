s = str(input())
a = 0
A = 0
for i in s:
    if 'a' <= i <= 'z':
        a += 1
    else:
        if 'A' <= i <= 'Z':
            A += 1
print(a, A)
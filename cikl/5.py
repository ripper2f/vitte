a = int(input())
chet = 0
nechet = 0
while a > 0:
    if a % 2 == 0:
        chet += 1
    else:
        nechet += 1
    a = a // 10
print(chet,nechet)
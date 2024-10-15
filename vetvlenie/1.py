a = int(input())
b = int(input())
c = int(input())
if abs(a) >= abs(c) and abs(a) >= abs(b):
    print(a)
elif abs(b) >= abs(c) and abs(b) >= abs(a):
    print(b)
else:
    print(c)
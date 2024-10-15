sequence = input("Введите скобочную последовательность: ")

stack = []

matching = True

for char in sequence:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack:
            matching = False
            break
        top = stack.pop()
        if (char == ')' and top != '(') or \
           (char == ']' and top != '[') or \
           (char == '}' and top != '{'):
            matching = False
            break

if stack:
    matching = False

if matching:
    print("Данная скобочная последовательность правильная.")
else:
    print("Данная скобочная последовательность неправильная.")
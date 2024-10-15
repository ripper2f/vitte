input_string = input("Введите строку: ")

string_without_spaces = ""
for char in input_string:
    if char != ' ':
        string_without_spaces += char

is_palindrome = True
length = len(string_without_spaces)

for i in range(length // 2):
    if string_without_spaces[i] != string_without_spaces[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
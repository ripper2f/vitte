input_string = input("Введите строку: ")

result_string = ""

for char in input_string:
    if char not in result_string and char != ' ':
        result_string += char

print(result_string)
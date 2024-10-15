a = input("Введите строку: ")

words = 0

in_word = False

for i in a:
    if i.isalnum():
        if not in_word:
            in_word = True
            words += 1
    else:
        in_word = False

print("Количество слов в строке:", words)
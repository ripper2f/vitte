a = input("Введите строку слов, разделенных пробелами: ")

max_length = 0
longest_words = []

for word in a.split():
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length
        longest_words = [word]
    elif word_length == max_length:
        longest_words.append(word)

if longest_words:
    for word in reversed(longest_words):
        print(word)
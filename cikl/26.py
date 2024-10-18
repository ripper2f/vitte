for number in range(1, 1001):
    str_number = str(number)
    num_digits = len(str_number)
    sum_of_powers = 0

    for digit in str_number:
        sum_of_powers += int(digit) ** num_digits

    if sum_of_powers == number:
        print(number)
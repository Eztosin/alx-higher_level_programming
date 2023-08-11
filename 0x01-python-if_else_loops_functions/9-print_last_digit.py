def print_last_digit(number):
    if number < 0:
        lastdigit = number % -10
    elif number >= 0:
        lastdigit = number % 10
    print("{:d}".format(abs(lastdigit)), end='')
    return abs(lastdigit)

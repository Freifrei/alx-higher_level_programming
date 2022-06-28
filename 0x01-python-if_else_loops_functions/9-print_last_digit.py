#!/usr/bin/python3
def print_last_digit(number):
    if numberr < 0:
        number = -number
    last = number % 10
    print(last, end='')
    return last

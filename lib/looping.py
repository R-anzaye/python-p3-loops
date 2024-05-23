#!/usr/bin/env python3
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    return print( "Happy New Year!")

happy_new_year()


def square_integers(int_list):
    return [x * x for x in int_list]

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    for num in range(1,101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()

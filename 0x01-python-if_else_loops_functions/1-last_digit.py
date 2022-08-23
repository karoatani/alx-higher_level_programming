#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numberx = ((number * -1) % 10) * -1
else:
    numberx = number % 10
if number > 5:
    print(f'Last digit of {number} is {numberx} and is greater than 5')
elif number == 0:
    print(f'Last digit of {number} is {numberx} and is 0')
elif number < 6 and (number % 10) != 0:
    print(f'Last digit of {number} is {numberx} and is less than 6 and not 0')

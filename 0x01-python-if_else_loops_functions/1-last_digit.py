#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
init = number % 10
if number < 0:
    init *= -1

if (number % 10) > 5:
    print(f"Last digit of {number} is {init} and is greater than 5")
elif (number % 10)  == 0:
    print(f"Last digit of {number} is {init} and is 0")
else:
    print(f"Last digit of {number} is {init} and is less than 6 and not 0")

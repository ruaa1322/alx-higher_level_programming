#!/usr/bin/python3
import random
import match
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
print(
        "last digit of {:d} is {:d} and is "
        .format(number,mod), end="")
if mod > 5:
    print("is greater than 5")
          
elif mod == 0:
    print("0")
else:
    print("less that 6 and not 0")

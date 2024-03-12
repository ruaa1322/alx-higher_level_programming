#!/usr/bin/python3
import random
import match
number = random.randint(-10000, 10000)
moo = number % 10 if number > 10 else number % -10
print(
        "last deget of {:d} is {:d} and is "
        .format(number,moo), end="")
if moo > 5:
    print("is greater than 5"
          
elif moo == 0:
    print("0")
else:
    print("less that 6 and not 0")

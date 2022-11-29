#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = str(number)[-1]

if int(lastdigit) > 5:
    print("Last digit of", number, "is", lastdigit, "and is greater than 5")
if int(lastdigit) == 0:
    print("Last digit of", number, "is", lastdigit, "and is 0")
if int(lastdigit) < 6 and lastdigit != 0:
    print("Last digit of", number, "is", lastdigit, "and is less than 6 and not 0")

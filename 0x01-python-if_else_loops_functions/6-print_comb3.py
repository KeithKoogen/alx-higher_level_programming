#!/usr/bin/python3
for i in range(9):
  for j in range(10 - i, 10):
    print("{ld}{rd}, ".format(ld = i, rd = j), end='')

print("89")
  

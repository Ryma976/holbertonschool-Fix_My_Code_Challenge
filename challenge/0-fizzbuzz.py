#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

n = int(sys.argv[1])

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

print()

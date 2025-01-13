#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:  # Handle the edge case of 0!
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

f = factorial(int(sys.argv[1]))
print(f)

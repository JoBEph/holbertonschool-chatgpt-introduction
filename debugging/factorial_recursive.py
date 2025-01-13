#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number n using recursion.

# Parameters:
# n (int): The number for which the factorial needs to be computed.

# Returns:
# int: The factorial of the input number n. If n is 0, it returns 1 as the base case.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main code to compute the factorial of a number passed via command line argument
f = factorial(int(sys.argv[1]))
print(f)


#!/usr/bin/python3
"""
This method calculates the fewest number of operations needed
to result in exactly n 'H' characters in the file.

Prototype: def minOperations(n)
Returns an integer.
If n is impossible to achieve, return 0.
"""

import math


def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n
    'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations required to achieve n characters.
    """

    # Check if n is less than or equal to 1, where the task is impossible
    if n <= 1:
        return 0

    # Initialize the operations count
    operations = 0

    # Iterate through potential factors of n, starting from 2
    factor = 2
    while factor * factor <= n:
        # If the current number is divisible by the factor
        while n % factor == 0:
            # Perform the Copy All and Paste operations
            operations += factor
            n /= factor
        factor += 1

    # If n is still greater than 1, it is a prime number
    if n > 1:
        operations += int(n)

    return operations

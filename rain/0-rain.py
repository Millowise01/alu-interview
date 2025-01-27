#!/usr/bin/python3
"""
0-rain
"""


def rain(walls):
    # Check if the input list is empty
    if not walls:
        return 0

    n = len(walls)  # Store the length of the walls list

    # Initialize two lists
    left_max = [0] * n
    right_max = [0] * n

    # Set the first element of left_max to the first wall height
    left_max[0] = walls[0]
    # Fill the left_max list by finding the maximum height so far from the left
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Set the last element of right_max to the last wall height
    right_max[n - 1] = walls[n - 1]
    # Fill the right_max list by finding the maximum height so
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Initialize total_water to 0, which will hold the total retained water
    total_water = 0
    # Calculate the retained water at each wall
    for i in range(n):
        # Add the water retained at wall[i i.e. the minimum of the maximum
        # to the left and right minus the current wall height
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water  # Return the total retained water

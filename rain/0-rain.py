#!/usr/bin/python3
"""Calculate rainwater retention between walls."""


def rain(walls):
    """
    Calculate total rainwater retained between walls.

    Args:
        walls (list): Heights of walls

    Returns:
        int: Total units of water retained
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water = 0

    # Calculate max height from left
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Calculate max height from right
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    # Calculate water trapped at each position
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > walls[i]:
            water += water_level - walls[i]

    return water

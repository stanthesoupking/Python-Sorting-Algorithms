"""
Bubble sort implementation
"""


def sort(values):
    """
    Sorts the given set of values using the bubble sort algorithm.
    """

    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(0, len(values) - 1):
            if values[i] > values[i + 1]:
                # Bubble up
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False

    return values

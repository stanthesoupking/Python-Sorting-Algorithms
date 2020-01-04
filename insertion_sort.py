"""
Insertion sort implementation
"""

def sort(values):
    """
    Sorts the given set of values using the insertion sort algorithm.
    """

    for i,x in enumerate(values):
        if i == 0:
            continue

        j = i - 1
        while j > -1:
            y = values[j]
            if x < y:
                # Swap
                values[j + 1] = y
                values[j] = x

                j -= 1
            else:
                break
    return values
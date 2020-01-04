"""
Insertion sort implemention
"""


def sort(values):
    """
    Sorts the given set of values using the selection sort algorithm.
    """

    s_pos = 0
    for x in values:
        # Find lowest value in unsorted sublist
        lowest = (s_pos, values[s_pos])
        for i, y in enumerate(values[s_pos:]):
            if y < lowest[1]:
                lowest = (s_pos + i, y)

        # Swap values
        values[s_pos] = lowest[1]
        values[lowest[0]] = x

        # Advance sorting position
        s_pos += 1
    return values

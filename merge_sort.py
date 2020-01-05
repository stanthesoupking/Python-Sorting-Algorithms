"""
Merge sort implementation
"""


def sort(values):
    """
    Sorts the given set of values using the merge sort algorithm.
    """

    # Values of length 1 = sorted
    if len(values) <= 1:
        return values
    else:
        # Split values in half and sort (divide & conquer)
        h = len(values) // 2
        s1 = sort(values[:h])  # Split 1
        s2 = sort(values[len(values) - h:])  # Split 2

        # Merge splits
        merged = []
        p1 = 0  # Position in split 1
        p2 = 0  # Position in split 2

        while p1 < len(s1) or p2 < len(s2):
            if p1 >= len(s1):
                merged.append(s2[p2])
                p2 += 1
            elif p2 >= len(s2):
                merged.append(s1[p1])
                p1 += 1
            elif s1[p1] < s2[p2]:
                merged.append(s1[p1])
                p1 += 1
            else:
                merged.append(s2[p2])
                p2 += 1

        return merged

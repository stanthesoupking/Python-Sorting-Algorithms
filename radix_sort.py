"""
Radix sort implementation
"""

import math

def sort(values):
    """
    Sorts the given set of values using the radix sort algorithm.
    """

    # Linear search through values to find maximum value size
    max_value = values[0]
    for x in values[1:]:
        if x > max_value:
            max_value = x

    # Create buckets
    bucket_depth = math.ceil(math.log10(max_value))
    buckets = []
    for i in range(0, bucket_depth):
        buckets.append([[] for x in range(0,10)])
    
    # Sort into initial buckets (first digit)
    for x in values:
        buckets[0][x % 10].append(x)

    # Populate buckets (digits following first digit)
    for i,bucket in enumerate(buckets):

        # Skip first digit (already sorted)
        if i == 0:
            continue

        for x in buckets[i - 1]:
            for y in x:
                bucket[(y // (10 ** i)) % 10].append(y)
    
    sorted_values = [y for x in buckets[len(buckets) - 1] for y in x]
    
    return sorted_values
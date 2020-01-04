"""
Radix sort implementation
"""

import math

def sort(values, bucket_count = 10):
    """
    Sorts the given set of values using the radix sort algorithm.
    """

    # Linear search through values to find maximum value size
    max_value = values[0]
    for x in values[1:]:
        if x > max_value:
            max_value = x

    # Create buckets
    bucket_depth = math.ceil(math.log(max_value, bucket_count) + 0.1)
    buckets = []
    for i in range(0, bucket_depth):
        buckets.append([[] for x in range(0,bucket_count)])
    
    # Sort into initial buckets (first digit)
    for x in values:
        buckets[0][x % bucket_count].append(x)

    # Populate buckets (digits following first digit)
    for i,bucket in enumerate(buckets):

        # Skip first digit (already sorted)
        if i == 0:
            continue

        for x in buckets[i - 1]:
            for y in x:
                bucket[(y // (bucket_count ** i)) % bucket_count].append(y)
    
    sorted_values = [y for x in buckets[len(buckets) - 1] for y in x]
    
    return sorted_values

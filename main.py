"""
Python Sorting Algorithms

A tool for comparing the speeds of various widely used sorting algorithms.
Algorithms are written in Python 3 and were tested using version 3.8.1.
"""

import argparse
import time
import insertion_sort, radix_sort

# Mapped algorithm name to sort function
# Note: Algorithm names must be in upper-case
available_algs = {
    'INSERTION': insertion_sort.sort,
    'RADIX': radix_sort.sort
}

# Create argument parser
parser = argparse.ArgumentParser(description='Python Sorting Algorithms')
parser.add_argument('--algorithm', type=str,
                    help='type of algorithm to employ')
parser.add_argument('--input', type=str,
                    help='input file to sort')
parser.add_argument('--output', type=str,
                    help='file to write sorted values into')
parser.add_argument('--time', const=True, nargs='?',
                    help='time the chosen sorting algorithm')

# Parse arguments
args = parser.parse_args()

# Check if supplied algorithm argument is valid
if isinstance(args.algorithm, str):
    args.algorithm = args.algorithm.upper()

if args.algorithm in available_algs:
    alg = args.algorithm
else:
    if args.algorithm != None:
        print('Invaild algorithm.')
    alg = None

while alg == None:
    # Query user for algorithm
    print('The following algorithms are available...')
    print(', '.join(sorted(available_algs)))
    print()
    x = input('Algorithm to employ: ').upper()

    if x in available_algs:
        alg = x
    else:
        print('Invalid algorithm.')

# Check if input file was specified
if args.input == None:
    input_path = input('Input file path: ')
else:
    input_path = args.input

# Check if output file was specified
if args.output == None:
    output_path = input('Output file path: ')
else:
    output_path = args.output

# Attempt to read input file
values = []
with open(input_path) as input_file:
    for line in input_file:
        values.append(int(line))

# Get initial time
if args.time:
    start_time = time.time()

# Sort
sorted_values = available_algs[alg](values)

# Get elapsed time
if args.time:
    elapsed = time.time() - start_time
    print(f'{elapsed:.2f} seconds elapsed.')

# Write output to file
with open(output_path, 'w') as output_file:
    for value in sorted_values:
        output_file.write(f'{value}\n')
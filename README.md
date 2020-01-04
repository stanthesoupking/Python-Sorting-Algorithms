# Python Sorting Algorithms

A tool for comparing the speeds of various widely used sorting algorithms. Algorithms are written in Python 3 and were tested using version 3.8.1.

## Usage
If ran without arguments such as below, options will be configured by console input at runtime:
```bash
python main.py
```

The full list of available options is as follows:
```
usage: main.py [-h] [--algorithm ALGORITHM] [--input INPUT] [--output OUTPUT] [--time [TIME]] [--radix-buckets RADIX_BUCKETS]

Python Sorting Algorithms

optional arguments:
  -h, --help            show this help message and exit
  --algorithm ALGORITHM
                        type of algorithm to employ
  --input INPUT         input file to sort
  --output OUTPUT       file to write sorted values into
  --time [TIME]         time the chosen sorting algorithm
  --radix-buckets RADIX_BUCKETS
                        the number of buckets to be used in each pass of radix sort
```
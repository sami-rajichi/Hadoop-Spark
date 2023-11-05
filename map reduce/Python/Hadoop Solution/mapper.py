#!/usr/bin/env python

# Import the sys module, which provides access to system-specific parameters and functions.
import sys

# Loop to process input lines from STDIN (standard input).
for line in sys.stdin:
    # Split the input line into individual tokens using tab ('\t') as the delimiter.
    tokens = line.split('\t')

    # Print specific tokens from the input line.
    # In this case, it prints the third token (index 2) and the second-to-last token (index -2).
    print(f'{tokens[2]}\t{tokens[-2]}')
#!/usr/bin/env python

import sys

# Initialize an empty dictionary to store cost totals for each store.
stores = {}

# Input comes from STDIN
for line in sys.stdin:

    # Create a dictionary 'stores' to accumulate costs for each store.
    store, cost = line.split('\t')

    # Update the cost for the corresponding store in the 'stores' dictionary.
    # If the store does not exist in the dictionary, initialize it with 0.0 and add the cost.
    stores[store] = stores.get(store, 0.0) + float(cost)

# Loop through the 'stores' dictionary to print the total cost for each store.
for store, cost in stores.items():
    print(f'{store}\t{cost}')
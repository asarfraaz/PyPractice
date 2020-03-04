"""
    Fetching lines from a file using Generator Functions
"""
# Copyright 2020 Sarfraaz Ahmed. All rights reserved.

from lines import get_lines
#from lines_gen import get_lines

from sys import getsizeof

with open("captains.txt") as FH:
    all_lines = get_lines(FH)
    print("Data size:", getsizeof(all_lines), "bytes")
    for line in all_lines:
        print(line)

# Copyright 2020 Sarfraaz Ahmed. All rights reserved.

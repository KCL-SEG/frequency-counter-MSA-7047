"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    str_list = [str(item) for item in items]    # turns all items to strings
    for item in str_list:
        count = 1
        if item in frequencies:                 # for any duplicate items
            count = frequencies.get(item) + 1
        frequencies.update({item: count})
    return frequencies
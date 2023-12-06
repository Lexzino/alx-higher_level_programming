#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary)
    for i in x:
        print("{}: {}".format(i, a_dictionary[i]))

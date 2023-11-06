#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        st = my_list[::-1]
        for num in st:
            print("{:d}".format(num))

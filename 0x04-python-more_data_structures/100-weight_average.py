#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum1 = sum(a * b for a, b in my_list)
        sum2 = sum(b for a, b in my_list)
        return sum1 / sum2
    else:
        return 0

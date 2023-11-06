#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final = []
    for number in my_list:
        if (number % 2) == 0:
            final.append(True)
        else:
            final.append(False)

    return (final)

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        temp = ""
        for k, v in a_dictionary.items():
            if k > temp:
                temp = k
        return temp
    else:

        return None

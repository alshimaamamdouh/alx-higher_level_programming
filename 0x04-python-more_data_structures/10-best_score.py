#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        temp_k = ""
        temp_v = 0
        for k, v in a_dictionary.items():
            if v > temp_v:
                temp_k = k
                temp_v = v
        return temp_k
    else:

        return None

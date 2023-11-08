#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    new_dic.update((k, v * 2) for k, v in new_dic.items())
    return new_dic

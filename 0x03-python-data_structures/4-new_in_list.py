#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        list_cp = my_list.copy()
        if idx < 0:
            return (my_list)
        elif idx > len(my_list) - 1:
            return (my_list)
        else:
            list_cp[idx] = element
            return (list_cp)

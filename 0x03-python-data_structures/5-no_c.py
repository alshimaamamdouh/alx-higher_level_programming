#!/usr/bin/python3
def no_c(my_string):
    st_new = ""
    for st in my_string:
        if st != 'c' and st != 'C':
            st_new += st

    return (st_new)

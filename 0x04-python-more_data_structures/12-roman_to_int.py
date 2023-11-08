#!/usr/bin/python3
def roman_to_int(roman_string):
    i = 0
    j = 0
    max = 0
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV', 'I')
    if type(roman_string) is not str:
        return 0
    elif roman_string is None:
        return 0
    else:
        while (i < len(ints)):
            for s in roman_string:
                if s == nums[i]:
                    max += ints[i]
                else:
                    max = max
            i = i + 1
        while (j < len(ints)):
            if roman_string == nums[j]:
                max = ints[j]
            j = j + 1
    return max

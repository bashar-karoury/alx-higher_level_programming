#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    current_rank = 0
    number = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for c in reversed(roman_string):
        if c in roman:
            rank = roman[c]
            if rank >= current_rank:
                number = rank + number
            else:
                number = number - rank
            current_rank = rank
        else:
            return 0
    return number

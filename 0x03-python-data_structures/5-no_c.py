#!/usr/bin/env python3

def no_c(my_string):
    updated_str = ''
    for i in my_string:
        if i != 'c' or i != 'C':
            updated_str += i
            return (updated_str)

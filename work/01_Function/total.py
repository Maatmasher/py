#! /usr/bin/env python3

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count+=number
    for key in keywords:
        count+=keywords[key]
    return count

print(total(10,1,2,3, vegitables = 50, fruits = 100))
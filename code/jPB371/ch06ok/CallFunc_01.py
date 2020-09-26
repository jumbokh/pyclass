# -*- coding: utf-8 -*-

def func(*num):
    total=0
    for n in num:
        total += n
    return total

print(func(1, 2))
print(func(1, 2, 3))
print(func(1, 2, 3, 4))


def func(**num):
    return num

print(func(a=1, b=2, c=3))

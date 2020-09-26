# -*- coding: utf-8 -*-

student = {'Judy': 90, 'Candy':46, 'Andy':69}

def x(d):
    print("**"+str(d[1]))
    return d[1]

print(sorted(student.items(), key =x))
# -*- coding: utf-8 -*-

student = {'Judy': 90, 'Candy':46, 'Andy':69}
print(sorted(student.items(), key = lambda x:x[1]))
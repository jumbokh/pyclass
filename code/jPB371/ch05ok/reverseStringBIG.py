# -*- coding: utf-8 -*-
letters = ""
for x in range(65, 91):
    letters += str(chr(x))
print(letters)

revletters = letters[::-1]
print(revletters)

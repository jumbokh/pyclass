# -*- coding: utf-8 -*-
letters = ""
for x in range(48, 58):
    letters += str(chr(x))
print(letters)

revletters = letters[::-1]
print(revletters)

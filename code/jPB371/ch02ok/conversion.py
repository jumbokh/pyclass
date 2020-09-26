# -*- coding: utf-8 -*-


str = "{1} + {0} = {2}"
a = 150
b = "60"
print( str )
print( str.format(a, b, a + int(b)) )
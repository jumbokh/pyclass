# -*- coding: utf-8 -*-

str1="Never say Never! Never say Impossible!"
str2="浪花有意千重雪，桃李無言一隊春。\n一壺酒，一竿綸，世上如儂有幾人?"
s1=str1.count("Never",15)
s2=str1.count("e",0,3)
s3=str2.count("一")
print("{}\n「Never」出現{}次,「e」出現{}次".format(str1,s1,s2))
print("\n{}\n「一」出現{}次".format(str2,s3))
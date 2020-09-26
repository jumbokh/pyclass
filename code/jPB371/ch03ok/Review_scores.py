# -*- coding: utf-8 -*-
"""
程式名稱：成績單統計小幫手
題目要求：
1.讀入CSV檔
2.列出總和、平均以及等級(甲、乙、丙、丁)
甲：平均80~100分
乙：平均60~79分 
丙：平均50~59分
丁：平均50分以下
"""
import csv

print("{0:<3}{1:<5}{2:<4}{3:<5}{4:<5}".format("", "姓名", "總分", "平均", "等級"))
with open("scores.csv",encoding="utf-8") as csvfile:
    x = 0
    for row in csv.reader(csvfile):
        
        if x > 0:
            scoreTotal = int(row[1]) + int(row[2]) + int(row[3])
            average = round(scoreTotal / 3, 1)
            
            if average >= 80 :
                grade = "甲"
            elif 60 <= average < 80:
                grade = "乙"
            elif 50 <= average < 60:
                grade = "丙"
            else:
                grade = "丁"
                
            print("{0:<3}{1:<5}{2:<5}{3:<6}{4:<5}".format(x, row[0], scoreTotal, average, grade))
         
        x += 1
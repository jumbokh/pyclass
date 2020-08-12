import csv
import random

with open('./H_7_4/H_7_4.csv','r') as fin:
    with open('./H_7_4/H_7_4_rand.csv','w',newline='') as fout:   #newline可以讓writerow輸出時不會有多餘的空白
        csvreader=csv.reader(fin,delimiter=',')
        csvwriter=csv.writer(fout,delimiter=',')
        header=next(csvreader)
        csvwriter.writerow(header)
        print(header)
        
        for row in csvreader:
            for i in range(1,len(row)):     #除日期外，從row[1]開始
                rnd=random.choice(("-1000","1000"))     #隨機產生1000或-1000的字串
                row[i]=int(row[i])+int(rnd)
            print(row)         
            csvwriter.writerow(row)
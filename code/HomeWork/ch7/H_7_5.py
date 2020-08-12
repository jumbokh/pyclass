with open('./H_7_5/H_7_5.txt','r') as fin:
    with open('./H_7_5/H_7_5_repNaN.txt','w') as fout:
        
        list1=[]
        count_line=0
        count_nan=0
        sum=0
        for line in fin:
            s=line.strip().split("\t")             #將每行字串以"\t"(一個tab)切割，並刪除空白符
            count_line=count_line+1                          #用以計算前行次數
            for i in range(0,len(s)):
                if(s[i]=="NaN"):
                    count_nan+=1
                    for j in range(1,count_line-1):            
                        sum=sum+int(list1[len(list1)-len(s)*j])  #取同一行前列的資料加總
                        s[i]=str(int(sum/(count_line-2)))        #講加總平均後取代NaN值
                    sum=0
                list1.append(s[i])                 #將數據存入list1中
            print(' '.join(s)+"\n")                #將切割過後的字串以' '(一個空白格)重新連接在一起，並在結尾加上'\n'換行
            fout.write(' '.join(s)+"\n")
        fout.write('總共缺值個數='+str(count_nan))
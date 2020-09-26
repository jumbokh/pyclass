print('PI = %10.5f'%(3.14159))	#輸出5位小數
print('PI = {0:010f}'.format(3.14159)) #前方補0欄寬10

radius = (3.14159) * 20 *20 #計算圓面積
area = int(radius) #將半徑轉換成整數
print('靠右 = {0:=>12d}'.format(area)) #*字元填滿
print('置中 = {0:=^12d}'.format(area))
print('PI = {0:.5f}\n'   
      '圓面積 = {1:,.4f}'.format(3.14159, radius)) 
      #圓面積加千位逗點
#圓面積以十進位、十六進位、二進位輸出
print('圓面積 = {0:d}, {0:#b}, {0:#x}'.format(area))

# H_5_8.py 功能:輸入開始及結束的停車時間，計算出停車費用並顯示
start = [] # 儲存開始的時間
end = [] #儲存結束的時間
start = str(input('開始停車時間 : '))
end = str(input('結束停車時間 : '))

# 將輸入字串的以"點"做分割
start = start.split("點")
end = end.split("點")

#區分早上、下午與小時數
start_list = [start[0][:2],start[0][2:]]
end_list = [end[0][:2],end[0][2:]]

#轉換為24小時制
if start_list[0] == "下午":
	start_hour = int(start_list[1])+12
else:
	start_hour = int(start_list[1])
	
if end_list[0] == "下午":
	end_hour = int(end_list[1])+12
else:
	end_hour = int(end_list[1])

#取出分鐘之數字，並轉換為整數
start_min = int(start[1].replace("分",""))
end_min = int(end[1].replace("分",""))

# 轉換成分鐘單位，並處理隔夜的狀況
if start_hour > end_hour:
	minute = (end_hour - start_hour + 24) * 60 + (end_min - start_min)
else:
	minute = (end_hour - start_hour) * 60 + (end_min - start_min)


# 判斷停車時間並計算費用
if minute <= 120 : # 兩小時以內
    cost = (minute // 30) * 30
elif minute >= 120 and minute <= 240 : # 兩小時以內但不超過四小時
    cost = 120 + ((minute-120) // 30) * 40
else : #超過四小時
    cost = 120 + 160 + ((minute-240) // 30) * 60
print('停車費用 : %d' %(cost))
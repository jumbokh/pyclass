tmp = bytearray(range(8))
#二進位資料的寫入
with open('bytedata', 'wb') as fob:
    fob.write(tmp)
#二進位資料的讀取
with open('bytedata', 'rb') as fob:
    fob.read(3)
    print(type(tmp))
    print('二進位：', tmp)

import random

def randint():
    print("執行了自訂的randint函數")

a = random.randint(0,99)  #使用random模組的randint函數
print("執行了random模組的randint函數：{}".format(a))

randint()  #呼叫自訂的randint函數

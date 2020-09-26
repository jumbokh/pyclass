try:
    score=eval(input("請輸入數字總和: "))
    total=eval(input("請輸入要求取平均的數字個數: "))
    ave=score/total
except ZeroDivisionError:
    print("")
except Exception as e1:
    print("錯誤訊息",e1.args)
else:
    print("沒有捕捉到例外, 所有數字的平均值= ", ave)
finally:
    print("成功離開此例外處理的區塊")

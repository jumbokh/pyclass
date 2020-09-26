while True:
    one, two = eval(
            input('請輸入兩個數值，用逗點隔開：'))
    try:
        result = divmod(one, two)      
    except ZeroDivisionError as err:
            print('錯誤', err)     
    else:
            print('計算結果', result)
            break
    finally:
            print('完成計算')

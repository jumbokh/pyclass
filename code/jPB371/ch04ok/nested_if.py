# -*- coding: utf-8 -*-
"""
巢狀if的綜合使用範例
"""
score = int(input('請輸入期末總成績：'))

# 第一層 if/else指令 判斷所輸入成績是否介於0到100之間
if score >= 0 and score <= 100:
    # 第二層 if/elif/else指令
    if score <60:
        print('{0} 分以下無法取得合格證書'.format(score))
    elif score >= 60 and  score <70: 
        print('{0} 分的成績等級是D級'.format(score))
    elif score >= 70 and  score <80:
        print('{0} 分的成績等級是C級'.format(score))
    elif score >= 80 and  score <90:
        print('{0} 分的成績等級是B級'.format(score))
    else:
        print('{0} 分的成績等級是A級'.format(score))
else:
    print('輸入錯誤, 所輸入的數字必須介於0-100間')

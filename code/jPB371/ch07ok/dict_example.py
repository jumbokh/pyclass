# -*- coding: utf-8 -*-

dictStr = {'bird':'鳥', 'cat':'貓', 'dog':'狗', 'pig':'豬'}
#新增wolf
dictStr['wolf']="狼"

#刪除pig
dictStr.pop("pig")

#列出dictStr所有的value
print("dictStr目前的元素：")
for v in dictStr.values():
    print(v) 

#搜尋
print("搜尋dog==>"+dictStr.get("dog","不在dictStr"))

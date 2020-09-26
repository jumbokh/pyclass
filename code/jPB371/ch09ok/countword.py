#定義函數用來計算所傳入字串中相同單字出現的字數
def check(string):
    wordlist = string.split()
    for word in wordlist:
        if word.lower() in mydict:
            mydict[word.lower()] = mydict[word.lower()] + 1
        else:
            mydict[word.lower()] = 1  

fb= open("exam.txt", "r")
text = fb.read()
fb.close()

mydict = {}
check(text)

for key in mydict:
    print("英文單字",key,"出現",mydict[key],"次")

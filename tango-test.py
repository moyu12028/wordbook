import json

word = []
flag = 1

try: #過去に生成したことある場合
    with open('word.json','r',encoding='utf_8')as file:
        word = (json.load(file)) #jsonの形式をlistに変換する
except: #最初の1回目の場合
    print('新規作成')
while 0 != flag:
    data = {}
    a = input('問題')
    b = input('答え')
    print(a)
    print(b)
    data['problem'] = a
    data['answer'] = b
    word.append(data)
    flag = int(input('継続するなら1,終了するなら0を入力'))
with open('word.json','w')as file:
    json.dump(word,file,indent=4,)
#coding:utf-8

import random

a = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

#テストのための答えを表示
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True:
    isok = False
    while isok == False:
        b = input('数を入れてね>')
        #4桁かどうか確認する
        if len(b) != 4:
            print("4桁の数字を入力してください")
        else:
            #数字かどうか確認する
            kazuok = True
            for i in range(4):
                if b[i]<'0' or b[i]>'9' :
                    print('数字ではありません')
                    kazuok = False # 数字ではないときはkazuokにFalseを設定する
                    break
            if kazuok :
                isok = True

    #4桁の数字であったとき
    #hitを判定
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit = hit + 1

        #blow = 0
        #for i in range(4):
            #if int(b[0] == a[i]) and (a[i] != int(b[i])) and (a[0] != int(b[0])): #被りなし、1桁目のhitなし
                #blow = blow + 1
                #break
        #for i in range(4):
            #if int(b[1] == a[i]) and (a[i] != int(b[i])) and (a[1] != int(b[1])): #被りなし、2桁目のhitなし
                #blow = blow + 1
                #break
        #for i in range(4):
            #if int(b[2] == a[i]) and (a[i] != int(b[i])) and (a[2] != int(b[1])): #被りなし、3桁目のhitなし
                #blow = blow + 1
                #break
        #for i in range(4):
            #if int(b[3] == a[i]) and (a[i] != int(b[i])) and (a[3] != int(b[1])): #被りなし、4桁目のhitなし
                #blow = blow + 1
                #break
    #ブローを判定
    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                blow = blow + 1
                break
    #結果を表示
    print('ヒット' + str(hit))
    print('ブロー' + str(blow))

    #ヒットが4なら当たりで終了
    if hit == 4:
        print('当たり！')
        break
import random

isok = False
while isok == False:
    b = input('数を入れてね>')
    if len(b) != 4:
        print("4桁の数字を入力してください")
    else:
        if b[0]<'0' or b[0]>'9' :
            print('数字ではありません')
        elif b[1]<'0' or b[1]>'9' :
            print('数字ではありません')
        elif b[2]<'0' or b[2]>'9' :
            print('数字ではありません')
        elif b[3]<'0' or b[3]>'9' :
            print('数字ではありません')
        else:
            isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

while isok == False:
    b = input('数を入れてね>')
    if len(b) != 4:
        print('4桁の数字を入力してください')
    else:
        kazuok = True
        for i in range(4):
            if b[i]<'0' or b[i]>'9' :
                print('数字ではありません')
                kazuok = False # 数字ではないときはkazuokにFalseを設定する
                break
        if kazuok :
            isok = True
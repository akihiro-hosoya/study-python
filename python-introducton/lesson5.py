#coding:utf-8

import random

a = random.randint(0,9)
print(a)

b = input('数を入れてね>') #文字列として認識されてしまう
if a == b:
    print('当たり')
else:
    print('はずれ')

b = int(input('数を入れてね>')) #数値として認識される
if a == b:
    print('当たり')
else:
    print('はずれ')


import random
a1 = random.randint(0,9)
a2 = random.randint(0,9)
a3 = random.randint(0,9)
a4 = random.randint(0,9)
print(str(a1)+str(a2)+str(a3)+str(a4)) #文字列で結合させないと足し算になってしまうから


#-----リスト-----
d = [6,8,0,2]
print(d[0])

a = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))
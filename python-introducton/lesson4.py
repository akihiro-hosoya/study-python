# coding:utf-8

a = 1
b = 2
print(a + b)

for i in [1,2,3,4,5]:
    print(i)
print('こんにちは')
for i in range(1,100+1):
    print(i)
print('こんにちは')
for i in range(0,100):
    print(i + 1)
print('こんにちは')
for i in range(100): # 省略形 for 変数名 in range(繰り返す回数)：
    print(i + 1)
for b in "Hello":
    print(b)

total = 0
a = 1
while total <= 50:
    total = total + a #total=0+1=1 total=1+2=3 total=3+3=6
    a = a + 1
    # 1+2+3+4+....が50以下なら繰り返す
print(total)#50を超えたときの値を表示

c = 1
while c <= 100:
    print(c)
    c = c+1

#while True:
    #実行したい文→永遠に繰り返し

#--------------if文----------------
for d in range(1,10+1):
    if d <= 5:
        print('小さいです')
    else:
        print('大きいです')

for e in range(1, 10+1):
    print(e)
    if e%2==0:
        print('○')
    if e%3==0:
        print('×')
    if (e%2==0) and (e%3==0):
        print('△')

for f in range(101):
    if f%12==0:
        print('0')
    else:
        if f%4==0:
            print('1')
        else:
            if f%2==0:
                print('2')
            else:
                print('3')
#elif
for g in range(101):
    if g%12==0:
        print(0)
    elif g%4==0:
        print(1)
    elif g%2==0:
        print(2)
    else:
        print(3)

#----------break--------
total = 0
h = 1
while True:
    total=total+h
    h=h+1
    if total>50:
        break
print(total)

#-----------関数----------

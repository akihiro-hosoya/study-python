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
print(total)　# 50を超えたときの値を表示
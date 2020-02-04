#coding:utf-8

#-----スコープ-----
a = "abc" #グローバルスコープ

def test():
    a = 'def' #testローカルスコープ
    print(a)
    return

test()
print(a)


def test():
    global a #global変数を使える
    a = 'def'
    print(a) #a='def'
    return

test() # def
print(a) # def


#-----可変長やオプションの引数-----
def tashizan (b, c=100):
    total = 0
    for i in range(101):
        total = total + i
    return total

d=tashizan(1)
print(d)


#-----モジュール-----
import calendar
print(calendar.month(2020,2))

import calendar as e
print(e.month(2020,3))
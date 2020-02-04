#coding:utf-8

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
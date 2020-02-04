#coding:utf-8

import random

isok = False #フラグ。最初はFalseにしておく
while isok == False: #Falseの間は繰り返す
    b = input('数を入れてね>') 
    if len(b) != 4:
        print('4桁の数字を入力してください')
    else:
        isok = True #正しく入力されたらフラグをTrueにする

print(b[0])
print(b[1])
print(b[2])
print(b[3])
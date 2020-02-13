# 関数の引数

# 位置関数とキーワード引数
# 実引数
def myfunc(param1, param2, param3):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'

# 位置引数
# これまでの呼び出し方
print(myfunc(1, 2, 3))
# 引数の位置に気を付ければ、特に問題なく引数を関数に渡せる

# キーワード引数
# 関数呼び出し時に「実引数をどのパラメーターに渡すべきか」を
# 「パラメーター名=実引数の値」のようにして指定
print(myfunc(param3=1, param2='string', param1=0.5))

# 位置関数とキーワード関数の混在
print(myfunc(1, param3='param3', param2=2))

# 引数のアンパック（展開）
# 反復可能オブジェクトの要素をアンパックして渡せる
'''
反復可能オブジェクトとは「その要素を1つずつ取り出せるオブジェクト」のこと。
文字列やリスト、辞書など
'''
# 位置引数
print(myfunc(*'abc')) # a,b,c
print(myfunc(1, *'23')) # 1,2,3
print(myfunc(*'12', 3)) # 1,2,3
# キーワード引数
# 「パラメーター名＝実引数の値」という形式にする必要あり
# 辞書（dictionary）などを使う必要あり
some_dict = {'key1':1, 'key2':'2'}
arg_dict = {'param3':'param3', 'param2':2, 'param1':1.0}
print(myfunc(**arg_dict)) # 辞書をアンパックしてmyfunc関数に渡す




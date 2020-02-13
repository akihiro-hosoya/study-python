# 可変長引数
# = 0個以上の引数
print('some')
print('some', 'value')
# 任意の数の位置引数を好きなだけ受け渡すための機構
# =「0個以上の引数」のこと
# formatメソッドも同様
# '{0} + {1} = {2}'.format(1, 2, 1+2)



# 可変長位置引数
def myfunc(param1, param2, *args):
    return f'param1: {param1}, param2: {param2}, other: {args}' # これで余計に引数を渡せる

print(myfunc(1, 2))  # 引数を2つだけ渡す
print(myfunc(1, 2, 3))  # 引数を3つ渡す
print(myfunc(1, 2, 3, 4))  # 引数を4つ渡す

# これは「タプル」のデータ構造になっている
def myfunc2(param1, param2, *args):
    tmp = f'param1: {param1}, param2: {param2}'
    index = 3  # 「paramX」という文字列を作成するのに使う
    for item in args:  # args（タプル）の各要素を取り出して文字列を作成
        tmp += f', param{index}: {item}'
        index += 1
    return tmp



# 可変長キーワード引数


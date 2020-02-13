# デフォルト引数値
# 実印数の指定を省略したときに、そのパラメーターに与えられる値
'''
デフォルト引数値は、関数を定義する際にパラメーターリストで
「パラメーター名=デフォルト引数値」とすることで指定できる。
'''
def myfunc(param1='param1', param2='param2', param3='param3'):
    return f'param1:{param1}, param2:{param2}, param3:{param3}'

# 引数を省略
print(myfunc())
# 第2引数と第3引数を省略
print(myfunc(1))
# パラメーターparam2の値だけを指定して、他は省略
print(myfunc(param2=2))

'''
パラメーターリストの中でいずれかのパラメーターにデフォルト引数値を指定したら、
それ以降（そのパラメーターよりも右側）のパラメーターにも
デフォルト引数値を指定する必要がある
'''

# print関数
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print('some', 'value')
# 一緒
import sys
print('some', 'value', sep=' ', end='\n', file=sys.stdout, flush=False)
print('some', 'value', sep='') # somevalue
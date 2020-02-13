# 関数の基本と呼び出し方

# 引数　→　関数　→　戻り値
# 変数名 = 関数名(引数1, 引数2, ...)

# 関数の定義
# def文
# def 関数名(パラメーター1, パラメーター2, ...):
#   関数で行う処理(関数ボディー(パラメーターの実数))
#   return 戻り値(変数でも計算式でも構わない)

# 簡単な関数
def hello(whom):
    message = 'Hello' + str(whom)
    print(message)

print(hello('World'))

# 戻り値
def get_ans4ultimateQ():
    return 42 # 関数の実行はここで終了
    # 戻り値として常に「42」を返す関数

    # print('can not reach this line')
    # この行は実行されない

# 呼び出し
print(get_ans4ultimateQ())
result = get_ans4ultimateQ()
print(result)
# ユーザー定義関数get_ans4ultimateQを呼び出して、その戻り値を変数resultに受け取るコード

# 関数の名前
# 関数名は、その関数が何をするものかを分かりやすく説明するものでなくてはならないので、このように長い名前になることがある。ただし、単に単語を連ねただけでは、読みづらい表記になってしまうので、必要に応じて、このようにアンダースコアを含めたり、短縮表記を用いたりすることがよくある。

"""
Pythonにおける「関数の命名規則」は
「PEP 8 -- Style Guide for Python Code」と呼ばれるドキュメント
で定められている。

関数名には英文字／アンダースコア／数字などを使えるが、
「PEP 8」で推奨されているのは「英小文字のみで構成し、
読みやすさを考慮して、適宜アンダースコアで単語をつなぐ」命名法
"""

# FizzBuzz問題
number = input('何か数値を入力してください：')
number = int(number)

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 ==0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)


# 関数バージョン
def fizzbuzz(number): # numberはパラメーター
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(str(number)) # str関数で文字列と数値のどちらにも対応できる
# これだけだと関数が実行されない
number = input('何か数値を入力してください：')
number = int(number)
print(fizzbuzz(number))
# Noneが表示されてしまう


# 修正
def fizzbuzz2(number): # numberはパラメーター
    result = str(number)
    if number % 3 == 0 and number % 5 == 0:
        result = 'FizzBuzz'
    elif number % 3 == 0:
        result = 'Fizz'
    elif number % 5 == 0:
        result = 'Buzz'
    return result # elseを使うとNoneが表示される
# これだけだと関数が実行されない
number = input('何か数値を入力してください：')
number = int(number)
print(fizzbuzz2(number))

"""
「def文で関数を定義した後でなければ、その関数を利用することはできない」
つまり、「関数は使う前に定義する」必要がある。
"""

# 関数のルール
print(some_func()) # 「Not defined」 となる

def some_func():
    print('you called some_func')
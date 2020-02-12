# エスケープシーケンス

# タブ文字
print('タブ\t文字')

# バックスラッシュ
print('バックスラッシュ\\')

# コードポイント
code_point = ord('a')

# 8進数値
oct_code = oct(code_point)
print(oct_code)
print('\141')

# 16進数値
hex_code = hex(code_point)
print(hex_code)
print('\x61')

# raw文字列
raw_str = r'https://www.atmarkit.co.jp/ait/articles/1904/16/news013_2.html'
print(raw_str)
raw_str

# 文字列と数値の変換
#user_input = input('input some number.')
#int_value = int(user_input)
#result = str(int_value) + '*2' + str(int_value * 2)
#print(result)

# len()
str_len = len('Hello World')
print(str_len)

# インデックス 文字列[index]
msg='Hello'
print(msg[0])
print(msg[len(msg)-1]) # 末尾の文字を取り出せる

# 文字列の結合
msg = 'Hello'"World"'''!Good-bye'''"""World"""
print(msg)

# in演算子 含まれているかどうか調べる
'Setagaya' in 'Sakura-Joushi, Setagaya-Ku, Tokyo, Japan'
'Setagaya' not in 'Sakura-Joushi, Setagaya-Ku, Tokyo, Japan'

# メソッド
# オブジェクト.メソッド名(引数)
sample_str = 'find, rfind, index, rindex'
# findメソッド
print(sample_str.find('index')) # 探してあれば最小のindex値が戻り値。なければ-1
# rfindメソッド
print(sample_str.rfind('index')) # 探してあれば最大のindex値が戻り値。なければ-1
# indexメソッド
print(sample_str.index('find')) # 探してあればその最小のindex値を、なければ例外（エラー）を発生させる
# rindexメソッド
print(sample_str.rindex('find')) # 探してあればその最大のindex値を、なければ例外（エラー）を発生させる

# 文字列の分割
# splitメソッド
# 戻り値は区切り文字で文字列を分割したものを格納したリスト
'abc def ghi'.split(' ')
'abc def ghi'.split(' ', 1) # 分割回数の指定
# joinメソッド
alpha_list = 'abc def ghi'.split() # 区切り文字の指定がないときは空白で区切れる
print(alpha_list)
alpha_str = ','.join(alpha_list)
print(alpha_str)

# 空白文字の削除
data = 'abc, def, ghi'
data_list = data.split(',')
print(data_list) # 空白ができてしまう
# stripメソッド
sample_str = ' sample '
print(sample_str)
print('begin:' + sample_str.strip() + '.end') # 先頭・末尾の空白削除
# lstripメソッド
print('begin:' + sample_str.lstrip() + '.end') # 先頭の空白削除
# rstripメソッド
print('begin:' + sample_str.rstrip() + '.end') # 末尾の空白削除
# 引数に任意の文字列を入れれば、それが削除対象になる

# 文字列の判定
# isdigitメソッド
num = 'not a number!'
user_input = input('input number:')
if user_input.isdigit():
    num = int(user_input)
print(num)

# 文字列の置換
sample_str = 'abc def GHI JKL'
# replaceメソッド 元の文字列.(元, 後, 回数)
print(sample_str.replace('abc', 'xzy'))
# swapcaseメソッド 元の文字列の大文字・小文字を入れ替える
print(sample_str.swapcase())
# titleメソッド 元の文字列に含まれている単語の先頭文字だけを大文字にする
print(sample_str.title())
# lowerメソッド 元の文字列に含まれている単語の先頭文字だけを大文字にする
print(sample_str.lower())
# upperメソッド lowerの逆
print(sample_str.upper())

# 特定の文字列で始まっている・終わっているか調べる
sample_str = 'this is a sample string.'
# startswithメソッド
print(sample_str.startswith('this'))
# endswithメソッド
print(sample_str.endswith('string'))

# 文字列を寄せる
sample_str = 'Python'
# 左寄せ ljustメソッド
print(sample_str.ljust(12, '+'))
# 中央寄せ centerメソッド
print(sample_str.center(12, '*'))
# 右寄せ rjustメソッド
print(sample_str.rjust(12))
# リストの基本
# 「配列」的な使い方をする

# リストの定義
languages = ['Python', 'Ruby', 'PHP']
print(languages)

# 使い方
for language in languages:
    print('Hello', language)

emptylist = [] # 空のリスト
print(emptylist)


# list関数
# list(反復可能オブジェクト)
strlist = list('Python') # 要素が'P', 'y', ... 'n'のリストを作成
print(strlist)
intlist = list(range(10)) # 整数値0〜9を要素とするリストを作成
print(intlist)
somelist = list(intlist) # リストからリストを作成（リスト内包表記）
print(somelist)



# リストの要素
# インデックス指定で文字列の要素を取得する
print(language[0])

somelist = ['python', 1, 100.5] # どんなデータもOK
print(somelist)

# リスト要素のスライス
intlist = list(range(10))
print(intlist[1:4])
print(intlist[:3])
print(intlist[5:])
print(intlist[1:9:2])

# リストの要素の変更
languages = ['Python', 'Ruby', 'PHP']
languages[2] = 'JavaScript'
print(languages)

intlist[0:10:2] = [10, 12, 14, 16, 18] # 先頭から1つ飛ばしで5個を変更
print(intlist)
#intlist[0:10:2] = [20, 22] # エラー：変更する要素の数だけ変更分がないといけない

# リストへの要素の追加
languages = ['Python', 'Ruby', 'PHP']
languages.append('Perl')
print(languages)



# リストの結合
cs = 'C#'
number = 99

languages = languages + [cs, number] # 結合
# languages + 'C++' はエラー：リストと文字列は結合できない。リスト同士のみ
print(languages)


# リストからの要素の削除
del languages[5] # delでインデックスを指定
print(languages)

languages.remove('PHP') # removeで削除したい値を指定
print(languages)

intlist = [1, 2, 3, 1, 2, 3]
intlist.remove(3)
print(intlist) # 最初の3が削除される

del languages
# print(languages) # リスト自体の削除



# リスト内包表記
'''
一般的な書き方 [要素を算出する式 for ループ変数 in 反復可能オブジェクト if 条件]
'''

# 要素数が多くなると、手で全ての要素を入力するのが面倒くさい
# for文を使って繰り返し処理を行うというのが一つの手として考えられる。

intlist = []
for num in range(10):
    intlist.append(num)
print(intlist)

# とはいえ、定形的に計算できる値を要素とするリストを作成するのに
# これだけの量のコードを書くのは面倒くさい

# そこで、上と同様なリスト作成をより簡潔に記述できるのが、「リスト内包表記」
intlist = [num for num in range(10)]
print([num*2 for num in range(10)])
print([num*num for num in range(10) if num%2==0])

for row in [[x*y for y in range(1,10)]for x in range(1, 10)]:
    print(row)
# xとyの繰り返しをずらしている(二重ループ)



# リストを要素とするリスト
result = []
for x in range(1, 10):
    # zを計算
    z = []
    for y in range(1, 10):
        z.append(x * y)
    result.append(z)

print(result[0][1])

for row in result:
    for column in row:
        print(f'{column:>3}', end='')
    print()
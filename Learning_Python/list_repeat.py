# リストの繰り返し処理

# for文でのリスト処理の基本
names = ['一色', '川崎', '遠藤']
for name in names:
    print(name)

intlist = [44, 99, 78, 36, 86, 100, 89, 48, 50, 58]
result = intlist[0] + intlist[1] + intlist[2] + intlist[3] + intlist[4] +\
        intlist[5] + intlist[6] + intlist[7] + intlist[8] + intlist[9]
print(result)
# これでは長い

result = 0
for number in intlist:
    result = result + number
print(result)
# リストの要素数が変わったときでも、for文でそれを処理する部分は同じコードで済む

# sum関数
# sum(iterable[, start])
# interable = 要素の総和を求めたい反復可能オブジェクト
# start = 総和にstartの値を合計したものが戻り値となる（省略可能）。
#         省略した場合は0を指定したものと見なされる
result = sum(intlist)
print(result)


#for文でリストの要素を変更する
languages = ['Python', 'Ruby', 'PHP']
print(languages)

for index in range(len(languages)): # lenで戻り値の3が渡される
    languages[index] = f'{index}: {languages[index]}'
print(languages)

# enumerate関数
# 反復可能オブジェクトとそのインデックスを利用したい場合に便利に使える
# enumerate(interable, start=0)
# interable = 要素とそのインデックスの両者を取り扱いたい反復可能オブジェクト
# start = インデックスの初期値。省略可能。省略時は「0」が指定されたものと見なされる

# for(インデックス, 要素) in enumerate(リスト):
#     for文の本体
languages = ['Python', 'Ruby', 'PHP']
print(languages)

for index, language in enumerate(languages):
    languages[index] = f'{index}: {language}' # languageリストではなくlanguagesリストの要素としている
print(languages)


# zip関数
# 2つ以上のリスト（などの反復可能オブジェクト）の要素をまとめたイテレータを作成
# zip(*iterable)
"""
複数の反復可能オブジェクトをカンマ区切りで指定する。
それらのインデックス0の要素をまとめたタプル、インデックス1の要素をまとめたタプル、……、
を返すイテレータが戻り値となる
同じインデックス位置にある名前と体重は「その人の名前と体重」の組を表すものとなる
"""
namelist = ['一色', 'かわさき', '遠藤', '島田', '小川']
weightlist = [65, 80, 70, 75, 72]
# これらのリストを関連づける
for name, weight in zip(namelist, weightlist):
    print(f'{name}さんの体重は{weight}kgです')

#引数として渡すリストの要素数に注意
shortlist = list(range(4))
longlist = list(range(10, 20))
for x, y in zip(shortlist, longlist):
    print(x, y)


# イテレータ、イテラブル（反復可能オブジェクト）
# イテレータ　＝　「データの流れを表現するオブジェクト」、反復可能オブジェクトの一種
# イテラブル　＝　「要素を一度に1つずつ返せるオブジェクト」
intlist = [0, 1, 2]
iterator = iter(intlist)

# print(iterator.__next__())
# print(next(iterator))
# print(iterator.__next__())
# print(nnext(iterator))
"""
要素が3つしかないのに、next関数と__next__メソッドを4回呼び出しているので、
エラーが発生しているのに注意
イテレータは「要素の反復取り出し」を全要素について一度は行ってくれるが、
全要素を取り出した後は、値を取り出そうとしても常にエラーとなる。

これに対して、リスト（などの反復可能オブジェクト）は常に各要素にアクセス可能である点にも注意しよう
"""


# map関数
# リストの各要素に対して、一定の処理を加えて得られた結果を要素とするイテレータを戻り値
# map(function, iterable, .....)
# functon = iterableの要素を引数に受け取り何らかの結果を返す関数。
#           iterableを複数指定したときには、functionはそれらの数だけ引数を持つ必要がある
# functionで処理をしたい反復可能オブジェクト

intlist = list(range(5))
result = map(lambda x: x*x, intlist)
print(intlist)
print(list(result))

result = [x*x for x in intlist]
print(result)
# [要素を算出する式 for ループ変数 in 反復可能オブジェクト if 条件]


# filter関数
"""
関数とリスト（反復可能オブジェクト）を引数に取り、
その関数にリストの各要素を渡して、
その結果が真となるものだけを要素とするイテレータを戻り値とする。
"""
intlist = list(range(10))
result = filter(lambda x: x%2==0, intlist) # x%2==0が関数
print(intlist)
print(list(result))

result = [x for x in intlist if x%2==0] # 偶数だけを選択
# [要素を算出する式 for ループ変数 in 反復可能オブジェクト if 条件]

# all関数とany関数
# all(interable)/any(interable)
# 全要素が真かどうか（all関数）／いずれかの要素が真かどうか（any関数）
# を調べたい反復可能オブジェクト
# TrueかFalseを戻り値とする
"""
空の反復可能オブジェクトを渡した場合には、
all関数はTrueを、any関数はFalseを戻り値とする
"""
intlist1 = list(range(5))  # [0, 1, 2, 3, 4]
intlist2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
intlist3 = [0] * 5  # [0, 0, 0, 0, 0]
strlist1 = ['', 'foo', 'bar']
strlist2 = ['foo', 'bar', 'baz']
strlist3 = [''] * 5
emptylist = []

print('all(intlist1):', all(intlist1))  # False：0は「偽」と見なされる
print('all(intlist2):', all(intlist2))  # True
print('all(intlist3):', all(intlist3))  # False：0は「偽」と見なされる

print('any(strlist1):', any(strlist1))  # True
print('any(strlist2):', any(strlist2))  # True
print('any(strlist3):', any(strlist3))  # False：空文字列は「偽」と見なされる

print('all(emptylist):', all(emptylist))  # True：空のリストを渡すと戻り値はTrue
print('any(emptylist):', any(emptylist))  # False：空のリストを渡すと戻り値はFalse

# 真ではないかどうかはnot any/not allを使う
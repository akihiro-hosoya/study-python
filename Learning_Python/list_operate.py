# リストの操作

# max,min関数
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
print(max(intlist))
print(min(intlist))
# keyパラメーター：絶対値基準
print('max(abs):', max(intlist, key=abs))
print('min(abs):', min(intlist, key=lambda x:-x if x<0 else x))
# defaultパラメーター
# iterableパラメーターが空のときに戻り値とする値をキーワード引数として渡す
# エラーを発生させないようにする
print(max([], default='no item'))
# 比較可能な要素ではいけない


#リストの結合・乗算
print([1, 2] + [3, 4])
print(5 * ['a'])


# in演算子
# 含まれているか
print('foo' in ['foo', 'bar'])
print('hoge' not in ['foo', 'bar'])


# indexメソッド
# 含まれているときに、それが何番目の要素であるか
# リスト.index(item, start, end)
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -9, 4]
# item=どこにあるのか
print(intlist.index(-9))
# start=検索を開始する位置wp示す
print(intlist.index(-1, 5))
# end=検索を終了する位置を示す
# print(intlist.index(4, 0, 9)):erorr


# countメソッド
# リスト.count(item)
# リストにitemが何個含まれているのか
print(intlist.count(1))
# indexメソッドとの混合
idx = -1
count = intlist.count(-9)
for num in range(count):
    idx = intlist.index(-9, idx + 1) # index[idx]以降を検索範囲とする
    print(f'{idx}: {intlist[idx]}')



# appendメソッド
# リスト.append(item)
# リストの末尾に要素「item」を追加する

# extendメソッド
# リスト.extend(iterable)
# リストの末尾に「interable」に含まれる全要素を追加する

intlist = list(range(5))
intlist.append(5)
intlist.append([6, 7])
intlist.extend([8,9])
print(intlist)


# insertメソッド
# リスト.insert(index, item)
# index = itemを挿入する位置
# item = 挿入する要素の値
intlist = list(range(5))
intlist.insert(2, 100)
print(intlist)



# リストからの要素の削除

# del文
# 指定したインデックス位置の要素を削除
foo = 'foo'
bar = 'bar'
baz = 'baz'
strlist = [foo, bar, baz]
print(strlist)
del strlist[1]
print(strlist)
print(bar) # 変数自体は消えない
# 「del strlist[1]」は「strlist[1]という名札を削除して、
# 文字列'bar'との関連付けを解除する」だけのもの

# removeメソッド
# リスト.remove(value)
# 「value」に等しい最初の要素をリストから削除する
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -9, 4, 0]
intlist.remove(-9) # 1つ目の-9しか消えない
print(intlist)
intlist.remove(False) # False=0
print(intlist)
# intlist.remove(100):入っていない値はエラー

# popメソッド
# リスト.pop(index)
# リストから「index」に指定した位置にある要素を削除して、
# その値を戻り値とする
intlist = list(range(5))
while intlist:
    print(intlist.pop()) # 省略した場合は「-1」が指定されたものとして。末尾の要素が削除される

# スタックとキュー
# スタック＝last-in, first-out：LIFO
# キュー＝first-in, first-out：FIFO

# clearメソッド
# リストの全要素の削除
intlist = list(range(10))
print(id(intlist)) # intlistのアイデンティテイーを表示
intlist.clear() # リストの全要素を削除
print(intlist)
print(id(intlist)) # intlistのアイデンティテイーは変わらない
intlist.append(5)
intlist = [] # intlistに空のリストを代入（リストを削除）
print(id(intlist)) # intlistのアイデンティテイーが変化する





# リストの並べ替え

# sortメソッド
# リスト.sort(key, reverse=False)
# リストを昇順に並べ替える
# key = 省略した場合は要素の値そのものを使って大小比較が行われる
#       指定した場合は、リストの要素をその関数に渡した結果を使って大小比較が行われる
# reverse = キーワード引数。Trueを指定するとリストを降順に並べ替える。デフォルト値はFalse
intlist = [6, 8, -2, 10, -3, 2, 5, 6, -9, 8]
intlist.sort()
print(intlist)

intlist = [6, 8, -2, 10, -3, 2, 5, 6, -9, 8]
intlist.sort(reverse=True) # 降順に並び替えられる
print(intlist)

intlist = [6, 8, -2, 10, -3, 2, 5, 6, -9, 8]
intlist.sort(key=abs) # 絶対値を元に並び替え
print(intlist)


# sorted関数
# 並び替えの結果だけを得たいとき
intlist = [6, 8, -2, 10, -3, 2, 5, 6, -9, 8]
result = sorted(intlist, key=abs)
print(intlist) # リスト自体の並びは変わらない
print(result)

strlist = ['abcd', 'abc', 'Abcd', 'abC']
print(sorted(strlist))
# 文字列を比較する際のルール
"""
コードポイントが小さいものほど小さい値とされる
2つの文字列の大小は先頭の文字、2文字目、3文字目……という順序で比較される
2つの文字列があり、それらの要素が途中までは全く同じだが、一方は最後に1文字だけ追加されている場合（上の'abc'と'abcd'）などは文字列が短い方が小さい値とされる
"""
print(sorted(strlist, key=str.lower)) # 全ての要素を小文字かときの並び替え順



# リストの反転

# reverseメソッド
# 反転したものが書き換わる
intlist1 = list(range(5))
print(intlist1)

intlist1.reverse()
print(intlist1)

# reversedメソッド
# 反転するが、リスト自体は置き換わらない
intlist2 = list(range(7))
intlist3 = list(reversed(intlist2))
print(intlist2)
print(intlist3)



# リストのコピー

# copyメソッド
# パラメーターなし、浅いコピー
strlist1 = ['foo', 'bar', 'baz']
strlist2 = strlist1.copy() # 浅いコピーの作成
strlist3 = strlist1 # intlist1とintlist3は同じリストオブジェクトを参照する

print(strlist1)
print(strlist2)

print(id(strlist1))
print(id(strlist2))
print(id(strlist3))

strlist1[0] = 'FOO'
print(strlist3) # ['FOO', 'bar', 'baz']
# 1と3は同じリストを参照しているから、
# strlit1の要素を変更すると、strlist3の要素も変更される

# 浅いコピー
intlist1 = [[1,2], [3,4], [5,6]]
intlist2 = intlist1.copy()

print(intlist1)
print(intlist2) # 1と同じ

print(id(intlist1))
print(id(intlist2)) # 1と異なる

intlist1[0][0] = 101
print(intlist1)
print(intlist2) # 1と同じ
"""
「浅いコピー」とは「オブジェクトへの参照をコピーする」
浅いコピーであるintlist2[0]でも同じ「[1, 2]」というリストを参照している
"""


# 深いコピー
from copy import deepcopy
intlist1 = [[1,2], [3,4], [5,6]]
intlist2 = deepcopy(intlist1) # deepcopy関数で「深いコピー」を行う

print(intlist1)
print(intlist2)

intlist1[0][0] = 101
print(intlist1)
print(intlist2) # 1とは異なる
"""
参照をコピーするのではなく、
参照をたどりながら最後の要素までコピーする方法のことを「深いコピー」と呼ぶ。

ただし、こちらは処理に時間がかかるなどの理由から、
プログラミング言語でリストのような多数の値を格納するデータ構造をコピーするときには
一般的に「浅いコピー」が行われるようになっている
"""
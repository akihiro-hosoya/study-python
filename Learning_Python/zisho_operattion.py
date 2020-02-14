# 辞書の操作
mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}

# len(辞書)
# 辞書の項目数

# del 辞書[キー]
# 辞書の項目を削除する

# key in 辞書 / key not in 辞書
# 指定したキーkeyが辞書に含まれているか / いないか

# 辞書.clear()
# 辞書の全項目を削除する

# 辞書.copy()
# 辞書をコピーする



# 辞書特有の操作

# updateメソッド
# 辞書に存在する項目を変更したり、辞書にない項目を追加したりといった操作を行える
# update([iterable][, **kwarg])
# iterable = 辞書の内容の更新する値を含んだ反復可能オブジェクト（省略可能）
"""
iterableが辞書の場合は、辞書にその項目の内容が反映される
（既存のキーについてはその値が変更され、新規のキーならその項目が追加される）

他の反復可能オブジェクトについては、その要素が「2つの要素を持つ反復可能オブジェクト」である必要がある。
その場合、最初の要素がキーに、次の要素がその値に見なされて、辞書の内容が更新される。
"""
# **kwarg = 「キー=値」形式のキーワード引数を任意の数だけ指定できる。
# この場合、「キー」が辞書のキーとして、「値」がその値として使われて、辞書の内容が更新される

mydict = {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
print(mydict)

mydict.update(foo='fooo', somekey='somevalue')
print(mydict)
mydict.update({'bar': 'new BAR'})
print(mydict)
mydict.update([('baz', 'new Baz'), ['x', 1]])
print(mydict)
mydict.update([('y', 2)], z=3)
print(mydict)


# popメソッド
# 指定したキーに関連付けられている値を得ると共に、
# そのキーと値の組を辞書から削除する
# pop(key[, default])
# key = その値を取得したいキー
# default = キーが辞書になかったときに返されるデフォルト値（省略可能）
# 省略した場合に、指定してkeyが辞書になければエラー（例外）が発生する
mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
print(mydict)

result = mydict.pop('bar')  # キー'bar'に対応する項目を削除
print(result)  # 削除した項目が戻り値になる
result = mydict.pop('bar', 'not found')  # デフォルト値を指定
print(result)  # キー'bar'はないので、デフォルト値が戻り値になっている
# result = mydict.pop('bar')  # キー'bar'はもう存在しないのでエラー


# popitemメソッド
# 辞書に登録されている項目の中から1つを削除して、
# そのキーと値の組（タプル）を戻り値とする
mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
print(mydict.popitem())
print(mydict.popitem())
print(mydict.popitem())
# print(mydict.popitem()) : 削除する項目がないのでエラー
# 辞書に追加したのとは逆の順序（Last In First Out、LIFO：後入れ先出し）で
# 項目が取り出されるようになっている



# setdefaultメソッド
# 辞書に特定のキーに関連付けられた値があるかどうかの存在確認を行い、
# あればその値を戻り値として、なければキーと値の組を新規に辞書に追加するもの
# setdefault(key[, default])
# key = 辞書に存在するか調べたいキー
# default = 辞書にキーが存在しなかったときに、追加する値（省略可能）
#           省略時にはNoneが指定されたものと見なされる
mydict = {'foo': 'foo', 'bar': 'bar'}
print(mydict.setdefault('foo'))  # 存在するキーを指定すれば、その値が返される
print(mydict.setdefault('baz', 'baz'))  # 存在しないキーは追加される
print(mydict)




# 辞書の項目の反復処理

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
for item in sk:
    print(item)
    # この場合には辞書のキーがループ変数に渡される

for item in sk:
    print(item, sk[item])
    # この方法もあるがあまり使われない

# keysメソッド
# 辞書に格納されているキーを一覧するビューオブジェクトを返す
# valuesメソッド
# 辞書に格納されている値を一覧するビューオブジェクトを返す
# itemsメソッド
# 辞書に格納されているキーと値の組を一覧するビューオブジェクトを返す

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
for key, value in sk.items():
    print(key, value)
"""
「ビューオブジェクト」は辞書に格納されているキーや値、あるいはそれらの組を一覧できる
動的なビューを提供するもので、今見たように反復可能オブジェクトのように扱える

「動的」というのは、ビューを作成した後に辞書に対して行われた変更が
キーに反映されることを意味している
"""
mydict = {'foo': 'foo'}
myview = mydict.keys()
print(myview)
mydict['bar'] = 'bar'
print(myview)
# ビューオブジェクトを得た後に辞書に追加した項目のキーも、
# ビューオブジェクトに含まれているのが分かる



# 辞書の使い所
"""
辞書は、
「格納されているデータに名前を付けることで扱いを容易にする」
「整数インデックスでは管理が難しいデータを扱う」ためのもの

リストはどちらかといえば「同種のデータを並べて管理する」もの
なので、あまりこのやり方はなじまない

タプルは異種データ（同種データでもよい）をひとまとめにして扱うのに便利なので、
上のような使い方をするのは普通のこと

タプルでは「何番目の要素が何を表すデータ」なのかが不明
"""

# 違い
page_data = {
    'https://www.atmarkit.co.jp/ait/articles/1906/14/news015.html':
    {
        'author': 'かわさき しんじ',
        'title': 'タプル',
        'pv': 123456
    },
    'https://www.atmarkit.co.jp/ait/articles/1906/13/news021.html':
    {
        'author': '一色 政彦',
        'title': 'Deep Learningコミュニティー……',
        'pv': 123456789
    },
    'https://www.atmarkit.co.jp/ait/articles/1906/04/news009.html':
    {
        'author': 'かわさき しんじ',
        'title': 'リストの操作',
        'pv': 1234567
    }
}

pv = 0
for key, value in page_data.items():
    if value['pv'] > pv:
        top_article = value
        top_article_url = key
        pv = value['pv']

print(f'top article is {top_article["title"]}')
print(f'top author is {top_article["author"]}')
print(f'top page view is {top_article["pv"]}')
print(f'top article url: {top_article_url}')

"""
このように、数値以外の（一意に特定可能な）何かのデータと、
それに対応する値を関連付けるといったときに辞書が役に立つ
"""


# 辞書のキーはイミュータブル
"""
辞書のキーとして使えるものは「変更不可能」（イミュータブル）なオブジェクトだけ

文字列（上記コード例のURLなど）やタプルなどは辞書のキーとして使えるが、
リストはその要素を変更できるのでキーには使えない。
辞書自体も要素の変更や追加、削除が可能なので、他の辞書のキーとして使うことはできない

# 以下は実行できない架空のコード
key_list1 = [0, 1, 2, 3]
key_list2 = [0, 1, 2, 1]
print(key_list1 == key_list2)  # False

mydict = {key_list1: 'foo', key_list2: 'bar'}
key_list1[3] = 1
print(key_list1 == key_list2)  # True
"""
# dictonary
# 「辞書」というのは、「キー」と「値」の組で表されるデータ（本稿ではこれを「項目」と呼ぶ）
# を複数格納可能なデータのこと

# 辞書の定義
sk = {'first_name':'shinji', 'family_name':'kawasaki', 'weight':80}

sk = {'first_name':'shinji', 'family_name':'kawasaki', 'weight':80, 'family_name':'okazaki'}
# 同じキーを2つ指定すると書き換わる

emptydict = {}
print(emptydict)



# dict関数
mydict = dict()
print(mydict)
# dict(**kwarg)
mydict = dict(foo='foo', bar='bar') 
print(mydict)
# kwarg = 「キーワード＝値」形式のキーワード引数。

# dict(mapping, **kwarg)
mydict = dict(foo='foo', bar='bar')
print(mydict)
# mapping = 辞書などの「キーと値の組」を持つマッピング型のオブジェクト
# 辞書を基にした辞書作成

# dict(iterable, **kwarg)
mydict = dict([('foo',1), ['bar', 2]])
print(mydict)
# iterable = 要素を2つだけ持つ反復可能オブジェクトを格納する反復可能オブジェクト
# 反復可能オブジェクトを使った辞書作成
mydict = dict({'foo':'FOO', 'bar':'BAR'}, baz='baz')
print(mydict)



# 辞書の内包表記
# {キーの算出式: その値を算出する式 for ループ変数 in 反復可能オブジェクト}
urls = ['https://someurl1', 'https://someurl2', 'https://someurls3']
pvs = [12345, 123456, 1234567]
authors = ['kawasaki', 'isshiki', 'endo']

pv_data = {u: {'pv':p, 'author':a} for u, p, a in zip(urls, pvs, authors)}
for key, value in pv_data.items():
    print(key, value['pv'], value['author'])


# 辞書の要素の取り出し
sk = {'first_name':'shinji', 'family_name':'kawasaki', 'weight':80}
print(sk['first_name'])
"""
Pythonのリストは整数値で要素をインデックス指定できる。
これに対して、辞書は任意の型の値をキーとして、それを用いて要素をインデックス指定するものとも考えられる。
ただし、リストやタプルとは異なり、辞書ではその要素をスライスすることはできない点には注意
"""
# print(sk['age]) : 存在しないキーを指定するとエラーになる


# getメソッド
# get(key[, default])
# key = その値を取得したいキー
# defaulr = キーが辞書になかったときに返されるデフォルト値（省略可能）
#           省略した場合にはNoneが指定されたものと見なされる
print(sk.get('first_name'))
print(sk.get('age'))
print(sk.get('age', 'not found')) # 存在しないキーと、デフォルト値を指定


# 辞書の項目の変更
sk['family_name'] = 'okazaki'
print(sk)
# 追加
sk['age'] = 150
print(sk)
# +演算子による辞書同士の加算などはできない

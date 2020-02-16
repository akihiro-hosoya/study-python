# クラスの属性

# Pythonのクラスには、これら以外にも以下に示す属性がある。

# クラス変数
# 「クラスに結び付けられた変数」のこと
# インスタンス変数　= インスタンスが持つデータを保存する
#                  クラス外部からのアクセス方法 = インスタンス.インスタンス変数
#                  クラス内でのアクセス方法 = self.インスタンス変数
# クラス変数 = クラスが持つデータや複数のインスタンスで共有するデータを保存
#             クラス外部からのアクセス方法 = クラス.クラス変数   インスタンス.クラス変数
#             クラス内でのアクセス方法 = self.クラス変数（値の書き換えに注意） 
#                                   クラス.クラス変数
#                                   self.__class__.クラス変数
#                                   type(self).クラス変数
class Point:
    pass
# インスタンスに属性(インスタンス変数)を与えるには、
point1 = Point()
point1.x = 1.0
point1.y = 1.0

# Pointクラスのインスタンスであるpoint1には独自の属性として、
# インスタンス変数x／yとhelloメソッドが与えられた。
# が、point2にはそうしたものはない
point1.hello = lambda x: print('Hello', str(x))
point1.hello('world')

# point2 = Point()
# point2.hello('world')  # エラー：Pointクラスの定義ではhelloメソッドはない

class MyClass:
    count = 0 # クラス変数countの定義

    def __init__(self):
        MyClass.count += 1 # クラス変数countにアクセス
        print(f'you made {MyClass.count} instance(s)')
    
    @classmethod # クラスメソッドの定義
    def get_count(cls):
        print(cls.count) # クラス変数には「cls.クラス変数」としてアクセス
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))
    
    @staticmethod
    def static_get_count():
        print('count:', MyClass.count)

instance1 = MyClass()
instance2 = MyClass()

print(MyClass.count)
instance = MyClass()
print(instance.count) # インスタンス.属性

instance.count = 100
print(instance.count)
print(MyClass.count)




# クラスメソッド
# 「クラスに結び付けられた関数（メソッド）」
"""
インスタンスではなく「クラス」と関連付けられている
「クラス.クラスメソッド(引数)」のようにして呼び出す
「そのクラスのインスタンスがなくても呼び出せる」ことが、インスタンスメソッドとの大きな違い

クラスメソッドは「インスタンス.クラスメソッド(引数)」という形でも呼び出せる
"""
"""
クラスメソッドの定義

まず「@classmethod」デコレーターを利用する方法を紹介
def文によるメソッド定義の前に「@classmethod」と書くだけ
クラスメソッドの第1パラメーターの名前は「cls」とすることが推奨されている

クラスメソッド関数でもOK
"""
MyClass.get_count()
MyClass.another_get_count()
instance1 = MyClass()
instance1.another_get_count()
instance1.get_count()



# スタティックメソッド
# 「クラスを名前空間として、その中に定義された関数（メソッド）」のようなもの
"""
スタティックメソッドを定義するには、
メソッドの前に「@staticmethod」を前置するだけ

第1パラメーターでクラスやインスタンスを受け取る必要はない。
そのため、クラス変数をスタティックメソッド内で参照するには「クラス.クラス変数」とするしかない

特定のインスタンスと結び付いているわけでもないので、インスタンス変数にアクセスすることもできない
"""
MyClass.static_get_count()
instance = MyClass()
instance.static_get_count()

# クラスの継承
"""
クラスとは「何らかのデータ（インスタンス変数）と、それらを処理するためのコード（メソッド）をひとまとめにして
名前を付けることで、後からそれらを再利用する」ための仕組み

「何らかのデータと、それらを処理するためのコード」を1つの単位（オブジェクト）として考え、
「さまざまなオブジェクトを、メソッド呼び出しを通じて、
どのように作用させていくかを記述することで、目前にある問題を解決する」プログラミング方法を
「オブジェクト指向プログラミング」と呼ぶ

Pythonでは全てのものが「オブジェクト」であり、本連載でこれまでに見てきたように、
文字列やリストなどの全てのオブジェクトにはデータとそれを処理するためのメソッドが備わっている
"""


# クラスを継承するとは？
"""
何らかのクラスからその属性を受け継ぐことを、プログラミングの世界では「継承」と呼ぶ。
実際には、クラスを「継承」するとは、元となるクラスの機能を受け継ぎながら、
そこに別の機能を付け足していくことでもある

継承元となるクラスのことを「基底クラス」「親クラス」「スーパークラス」などと呼び、
継承先となるクラスのことを「派生クラス」「子クラス」「サブクラス」などと呼ぶ

〇〇クラスはobjectクラスの派生クラスであると同時に、objectクラスとしても扱える。
このことから、「Pointクラスはobjectクラスである」ともいえる。
このような継承関係のことを「is-a」の関係と呼ぶ
"""

# オブジェクトの型
"""
「シーケンス」と呼ばれるデータ型について
これらはシーケンス型という大枠に属するが、それぞれが異なる特性を持つ。

リスト：変更可能なシーケンス。任意の型のオブジェクトを要素にできる
タプル：変更不可能なシーケンス。任意の型のオブジェクトを要素にできる
文字列：変更不可能なシーケンス。Unicodeのコードポイントを要素とする


変更可能なシーケンスは「変更不可能なシーケンスと共通な特性」を持ち、
それに対して「要素を変更するための属性を付け加えたもの」である。

「共通な特性」とは「インデックスアクセス」「反復可能」「要素の存在確認」などであり、
「付け加えたもの」とは「要素への代入」「要素の削除」などである。

こうしたことを考えると、変更可能なシーケンスは、
変更不可能なシーケンスを継承（拡張）したものだと捉えるのが適切


・基底クラス（継承階層で上位に位置するクラス）は
    より抽象的な（多くのクラスで共通する）概念を表現する
・派生クラス（継承階層で下位に位置するクラス）は基底クラスが持つ特性を継承して、
    それを改変したり、拡張したりする（抽象的なクラスをより具体的なクラスにしたり、
    特性の異なるさまざまなクラスを定義したりしていく）
"""


# クラス継承の方法
"""
def クラス名（基底クラス）:
    # クラス定義の本体
クラスを1つだけ指定する場合を「単一継承」と呼び、複数のクラスを指定する場合を「多重継承」と呼ぶ
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name # インスタンス変数nameにその人の名前を
        self.age = age # インスタンス変数ageにその人の年齢を
    def hello(self):
        print('Hello,', str(self.name)) # 「Hello ○○」と画面に表示するインスタンスメソッド
    def get_age(self):
        return self.age # 年齢を知るためのget_ageメソッド
# Personクラスのインスタンス
kawasaki = Person('kawasaki', 250)
isshiki = Person('isshiki', 19)
kawasaki.hello()
print(isshiki.get_age())

# Personクラスを継承するStudentクラスを定義する
class Student(Person):
    # 派生クラスに属性を追加する
    # メソッドのオーバーライド
    def __init__(self, name, age, school):
        # super関数
        super().__init__(name, age) # 基底クラスで定義されるインスタンス変数の初期化を行っている
        self.school = school
    # 基底クラスで定義されているものと同名のメソッドを派生クラスで定義することを
    # 「メソッドをオーバーライド（上書き）する」という
    def get_school(self):
        return self.school
    def hello(self): # オーバーライド
        super().hello()
        print('You are a student of', self.school)
    """
    __init__メソッドをオーバーライドするときに注意したいのは、「Student(……)」のようにして
    Studentクラスのインスタンスを生成すると、Pythonによって__init__メソッドが自動的に呼び出されるが、
    この際に基底クラスであるPersonクラスの__init__メソッドは呼び出されなくなってしまう点だ

    簡単にいうと、Personクラスの__init__メソッドで行っていたインスタンスの初期化処理は行われなくなってしまうということ

    そのために上では、Personクラスのインスタンス変数とStudentクラスのインスタンス変数の3つを初期化するようになっている
    """

# PersonクラスとStudentクラスのインスタンスを作る
isshiki = Student('isshiki', 18, 'Imperial univ')
isshiki.hello()
print(isshiki.get_school())




# クラスやインスタンスが特定のクラスに属するかを調べる

# isinstance関数
# isinstance(obj, class)
# obj = パラメーターclassに指定されたクラスまたはその派生クラスのインスタンスかどうかを調べたいオブジェクト
# class = パラメーターobjに与えられたオブジェクトが、特定のクラスまたはその派生クラスのインスタンスかどうかを調べる対象。
#         複数のクラスをタプルとして渡してもよい

# issubclass関数
# issubclass(class1, class2)
# class1 = パラメーターclass2に指定されたクラスまたはその派生クラスであるかどうかを調べたいクラスを指定する
# class2 = パラメーターclassに受け取ったクラスが、特定のクラスまたはその派生クラスであるかどうかを調べる対象。
#          複数のクラスをタプルとして渡してもよい

# 例
# 整数値「100」はfloat型のインスタンスか
print('isinstance(100, float):', isinstance(100, float))
# studentはPersonクラスのインスタンスか
student = Student('isshiki', 18, 'Imperial univ')
print('isinstance(Student, Person):', isinstance(student, Person))
# StudentクラスはPersonクラスの派生クラスか
print('issubclass(Student, Person):', issubclass(Student, Person))

# スタック

# 定義
# プッシュ push(self, item)
# itemに受け取ったデータをインスタンス変数stackに追加する。戻り値はなし

# ポップ pop(self)
# インスタンス変数stackの末尾のデータを取り出す。
# その後、対応する要素をリストから削除し、取り出したデータを戻り値として返送する

# データの保存先（インスタンス変数） stack
# 最初は空のリストとして作成し、それに対してデータを追加したり、取り出したりする。
# コード内ではself.stackとして参照することを忘れないようにすること


"""
スタックは「データを積み重ねたもの」と述べたが、ここではそれをリストとして表現している
"""

class MyStack:
    def __init__(self):
        self.stack = [] # 空のリストをスタックに保存するデータの入れ物とする
    # pushメソッドの定義
    def push(self, item): # appendメソッドかextendメソッドを使う
        self.stack.append(item)
    # popメソッドの定義
    # リストの末尾のデータを一時的に変数に代入して、リストからその要素を削除して、
    # 最後に取り出しておいたデータを戻り値として返送すればよい
    def pop(self):
        if len(self.stack) == 0:
            return None # ないときはNoneを返せる
        result = self.stack[-1]  # 末尾の要素を変数に取り出す
        del self.stack[-1] # リストから要素を削除する
        return result # リスト末尾から取り出したデータを返送する
        # return self.stack.pop() でもOK

# pushの確認
mystack = MyStack()
mystack.push(0) # スタックに「0」をプッシュ（リストの末尾に「0」を追加）
mystack.push(1)
mystack.push(2)
print(mystack.stack) # MyStackクラスのインスタンスのインスタンス変数の値を表示

# popの確認
print(mystack.pop()) # 末尾から削除されていく
print(mystack.pop())
print(mystack.pop())



# キューを定義する
"""
キューはスタックとは違って、最初にキューに置かれたものが、最初に出てくる
"""
class MyQueue:
    def __init__(self):
        self.queue = []
    # エンキュー enqueue(self, item)
    # itemに受け取ったデータをインスタンス変数queueに追加する。戻り値はなし
    def enqueue(self, item):
        self.queue.append(item)
    # デキュー dequeue(self) 
    # インスタンス変数queueから先頭のデータを取り出す。
    # その後、対応する要素をリストから削除し、取り出したデータを戻り値として返送する
    def dequeue(self):
        if len(self.queue) == 0:
            return None
    # データの保存先（インスタンス変数）queue
    # 最初は空のリストとして作成し、それに対してデータを追加したり、取り出したりする。
    # コード内ではself.queueとして参照することを忘れないようにすること
        result = self.queue[0]
        del self.queue[0]
        return result

myq = MyQueue()
myq.enqueue(0)
myq.enqueue(1)
print(myq.dequeue())
print(myq.dequeue())
print(myq.dequeue())



# スタックをより使いやすくする
# 「特殊メソッド」でPythonの組み込み型（リストなど）と似た使い勝手になる

# 特殊メソッド
mystack = MyStack()
print(str(mystack)) # オブジェクトの「非公式な文字列表現」を得るもの
print(repr(mystack)) # オブジェクトの「公式な文字列表現」を得るもの


# インスタンスの生成時に初期値を与える
# MyStackクラスのインスタンス生成時に、その初期値を与えると、
# それを要素とするスタックが作成されると便利かもしれない
"""
既に定義している__init__メソッドを変更して、
MyStack()呼び出しで引数を指定できるようにすればよい。

　ただし、__init__メソッドの定義を修正する前に考えておくことがある
それは引数の受け渡しをどのように行い、それらを基にスタックの初期値をどのように設定すればよいか

任意の数の引数をカンマ区切りで渡す
カンマで区切られた引数はそれぞれが個別にスタックの要素となる

これを実現するには、可変長位置引数を使えばよい
"""
class MyStack2:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack2(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)
    def __getitem__(self, key):
        return self.stack[key]

mystack2 = MyStack2(1, 2, [3, 4])
for item in mystack2:
    print(item)
print(mystack2.stack)
print(repr(mystack2))
print(mystack2)
print(mystack2[0:2])

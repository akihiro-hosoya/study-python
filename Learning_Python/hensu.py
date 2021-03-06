# ローカル変数
def myfunc():
    a = 'Python'
    print('a:', a)

# これだけだとエラーが出る
a = 'Python'

myfunc()
print(a) # ここではローカル変数はつかえない

# 名前解決
"""
「変数に代入をするときには、通常、ローカルスコープから使われる」
"""
# 1.ローカルスコープ→ローカル変数bはない→×
# ローカルスコープで名前が見つからなければ、次にグローバルスコープから「b」という名前が探される。
# 2. グローバルスコープ→グローバル変数bがある→解決終了

# ローカルスコープ → グローバルスコープ → ビルトインスコープ


# 名前空間
# 「名前」と「その値」を関連付けるもの
"""
ビルトイン名前空間：Pythonインタープリタの起動時に作成され、インタープリタ終了時に削除される
グローバル名前空間：モジュール読み込み時に作成され、多くの場合はインタープリタ終了時に削除される
ローカル名前空間：関数が呼び出されるタイミングで作成され、終了時に削除される
"""

__name__ # 現在のモジュール名がわかる

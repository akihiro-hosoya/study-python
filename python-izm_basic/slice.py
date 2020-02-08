# スライス
# スライスの基本

# seaquence[<開始位置>:<終了位置>:<ステップ幅>]
test_list = ['https', 'www', 'python', 'izm', 'com']
print(test_list[:])
print(test_list[::])

# 要素の取得
print(test_list[:4])  # 開始位置を省略 → 先頭から指定位置までの要素を取得
print(test_list[2:])  # 終了位置を省略 → 指定位置から末尾までの要素を取得
print(test_list[::2]) # ステップ幅を指定 → 指定数ごとの要素を取得
print(test_list[3:5]) # 開始から終了までの範囲内の要素を取得
    # 「-」を使えば末尾から取得できる
print(test_list[-1:])  # 末尾から全ての要素
print(test_list[:-1])  # 末尾までの全ての要素
print(test_list[::-1]) # 末尾からの全ての逆要素順
    # 要素数を超過していてもカットされる
print(test_list[:999])

# 要素の代入
test_list[1:3] = ('WWW', 'PYTHON')
print(test_list)



# コメントアウト
# 複数行の場合
# ’’’
# print('test 3')
# print('test 4')
# '''
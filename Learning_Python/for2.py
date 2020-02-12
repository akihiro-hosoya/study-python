# for文
# 繰り返し処理はforかwhile

# 基本構文
message = 'Hello Python'

for ch in message: # for ループ変数 in 反復可能オブジェクト;
    print(ch)


# for文とrange関数
# range(stop)
for number in range(10):
    print(number)

message = 'Hello Python'
str_count = len(message)
for index in range(str_count): # for ループ変数 in 反復可能オブジェクト;
    print(message[index])

# for文のelse節
"""
for ループ関数 in 反復可能オブジェクト:
    ブロック
else:
    反復処理終了時に実行するブロック
"""
for num in range(5):
    print(num)
else:
    print('terminated')

# for文とリスト
names = ['一色', 'かわさき', '遠藤']
target = 'かわさき'
for name in names:
    if target in name:
        print(f'発見:{name}')
    else:
        print('見つかりませんでした')
        # これだけだとどちらも表示されてしまう　→　繰り返し処理が終わっていないから

for name in names:
    if target in name:
        print(f'発見:{name}')
        break # これで終わる
else:
    print('見つかりませんでした')


# continue文
names = ['一色', 'かわさき', 'かわさきしんじ', '遠藤']
target = 'かわさき'
for name in names:
    if target in name:
        print(f'発見:{name}')
        continue # breakだと2つ目で終わってしまう
    print('繰り返し処理を継続します')
else:
    print('見つかりませんでした') # これも表示されてしまう
    

# continue文　修正
names = ['一色', 'かわさき', 'かわさきしんじ', '遠藤']
target = 'かわさき'
found = False

for name in names:
    if target in name:
        found = True
        print(f'発見:{name}')
        continue # breakだと2つ目で終わってしまう
    print('繰り返し処理を継続します')

if not found:
    print('見つかりませんでした')
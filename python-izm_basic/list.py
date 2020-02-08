# リスト
test_list_1 = ['python', '-', 'izm', '.', 'com']
print(test_list_1)

for i in test_list_1:
    print(i)

# 要素の追加
test_list_1 = []
print(test_list_1)

test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')
print(test_list_1)

#インデックスを指定して追加
test_list_1 = ['python', 'izm', 'com']

test_list_1.insert(1, '-')
test_list_1.insert(3, '.')
print(test_list_1)

test_list_1.insert(0, 'http://www.')
print(test_list_1)

# 要素の削除1
test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

test_list_1.remove('2')
print(test_list_1)

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1.pop(1)) # '2'が削除 
print(test_list_1)

print(test_list_1.pop()) # 末尾が削除
print(test_list_1)

# 要素のインデックスを取得
test_list_1 = ['100', '200', '300', '200', '100']
print(test_list_1.index('200')) # 最初のインデックス値のみ返される

# リスト内での要素数を取得
print(test_list_1.count('200'))


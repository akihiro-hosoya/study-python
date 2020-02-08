# 文字列
print('python-izm')
print("python-izm")
test_str = """
test_1
test_2
"""
print(test_str)

# 連結
test_str = 'python'
test_str = test_str + '-'
test_str = test_str + 'izm'
print(test_str)

test_str = '012'
test_str += '345'
test_str += '678'
test_str += '9'
print(test_str)

test_str = '012'*3
print(test_str)

# 文字列へ変換
test_integer = 100
print(str(test_integer) + '円')

# 連結
test_str = 'pyrhon-izm'
print(test_str.replace('izm', 'izm'))

# 分割
test_str = 'python-izm'
print(test_str.split('-'))

# 桁揃え
test_str = '1234'
print(test_str.rjust(10, '0'))
print(test_str.rjust(10, '!'))

print(test_str.zfill(10))
print(test_str.zfill(3))

# 検索
test_str = 'python-izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

print('z' in test_str)
print('s' in test_str)

# 大文字・小文字変換
test_str = 'Python-Izm.Com'
print(test_str.upper())
print(test_str.lower())

# 先頭の削除
print('----------------------')
test_str = '     python-izm.com'
print(test_str)
test_str = test_str.lstrip()
print(test_str)
print('----------------------')

# 末尾の削除
test_str = 'python-izm.com     '
print(test_str + '/')
test_str = test_str.rstrip()
print(test_str + '/')
test_str = test_str.rstrip('com')
print(test_str)

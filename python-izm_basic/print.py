print('python', end=' ')
print('-', end=' ')
print('izm', end=' ')
print('.', end=' ')
print('com')

# 出力先の変更
f_obj = open('test.txt', 'w')
print('python-izm.com', file=f_obj)


# フォーマット出力
print('Pythonの学習サイト：{}'.format('python-izm.com'))
print('Pythonの学習サイト：{0}-{1}-{2}'.format('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設　{0} 日目！ {1}'.format(test_int, test_str))
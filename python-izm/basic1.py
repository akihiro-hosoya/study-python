print('python-izm')
print("python-izm")
test_str = """
test_1
test_2
"""
print(test_str)

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

test_integer = 100
print(str(test_integer) + '円')

test_str = 'pyrhon-izm'
print(test_str.replace('izm', 'izm'))

test_str = 'python-izm'
print(test_str.split('-'))

test_str = '1234'
print(test_str.rjust(10, '0'))
print(test_str.rjust(10, '!'))

print(test_str.zfill(10))
print(test_str.zfill(3))

test_str = 'python-izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

print('z' in test_str)
print('s' in test_str)

test_str = 'Python-Izm.Com'
print(test_str.upper())
print(test_str.lower())

print('----------------------')
test_str = '     python-izm.com'
print(test_str)
test_str = test_str.lstrip()
print(test_str)
print('----------------------')

test_str = 'python-izm.com     '
print(test_str + '/')
test_str = test_str.rstrip()
print(test_str + '/')
test_str = test_str.rstrip('com')
print(test_str)

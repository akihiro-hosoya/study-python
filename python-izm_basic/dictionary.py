# ディクショナリの基本
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)

print('======================================')

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('----------------------------------------')



# valueの取得
print(test_dict_1['YEAR'])
#print(test_dict_1['YEARS'])

print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS')) # getならkeyが存在しなくてもエラーにならない

print(test_dict_1.get('YEAR', 'NOT FOUND'))
print(test_dict_1.get('YEARS', 'NOT FOUND')) # keyが存在しなかった場合のデフォルト値を設定できる



# 要素の追加
test_dict_1 = {}
print(test_dict_1)

test_dict_1['YEAR'] = '2010'
test_dict_1['MONTH'] = '1'
test_dict_1['DAY'] = '20'
print(test_dict_1)


# 要素の削除
print(test_dict_1)

del test_dict_1['DAY']
print(test_dict_1)


# keyやvalueだけを取得する
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)

print(test_dict_1.keys()) # keyだけを取得
print(test_dict_1.values()) # valueだけを取得


# keyを保持しているかの確認
print('YEAR' in test_dict_1)
print('YEARS' in test_dict_1)
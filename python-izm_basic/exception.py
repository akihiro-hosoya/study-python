# 例外処理

# try, expect, finally
def exception_test(value_1, value_2):

    print('＝＝＝＝計算開始＝＝＝＝')

    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算できませんでした！')
    finally:
        print('計算終了')

    return result

print(exception_test(100,200))
print(exception_test(100, '200'))



# raise
def exception_test2(value_3, value_4):

    print('＝＝＝＝計算開始＝＝＝＝')

    result2 = 0

    try:
        result2 = value_3 + value_4
    except:
        print('計算できませんでした！')
        raise
    finally:
        print('計算終了')

    return result2

try:
    print(exception_test2(100,200))
    print(exception_test2(100, '200'))
except:
    print('エラーを受け取りました')



# エラー内容の取得
import sys
import traceback

def exception_test3(value_5, value_6):
    print('＝＝＝＝計算開始＝＝＝＝')

    result3 = 0

    try:
        result3 = value_5 + value_6
    except:
        print('計算できませんでした！')
        raise
    finally:
        print('計算終了')

    return result3

try:
    print(exception_test3(100, '200'))
except:
    print(traceback.format_exc(sys.exc_info()[2]))
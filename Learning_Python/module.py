# モジュールとは
"""
プログラム中で何度も利用するコードを1つにまとめる
まとまったコードの固まりに名前を付けて、コードの意図を分かりやすくする
プログラムを関数の形で他のプログラムから利用できるようにする

コードの再利用（一度書いたプログラムの別のプログラムからの利用）が可能になる



意味的に関連性がある関数などをまとめるのが一般的。
例えば、数学関数（絶対値、三角関数など）をまとめたモジュールや、HTTP通信を行うためのモジュールなどが考えられる
"""

# import
# import module_name

import random as rnd
print(rnd.randint(1, 20))

# importはまとめてやらない


# import as文
# 指定した名前でインポート
import numpy as np


# from import文
# 特定の関数だけをimport
# from module_name import identifier

from random import randrange, randint
# randomモジュールのrandintだけをimport
print(randint(1, 20))




import matplotlib.pyplot as plt
def fit(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    x_centered = [item - x_mean for item in x]
    y_centered = [item - y_mean for item in y]

    xy = [item_x * item_y for item_x, item_y in zip(x_centered, y_centered)]
    xx = [item * item for item in x_centered]
    sum_xy = sum(xy)
    sum_xx = sum(xx)

    a = sum_xy / sum_xx
    b = y_mean - a * x_mean

    return (a, b)

# サンプルデータ
x = [-0.03, 0.78, 2.07, 2.77, 4.10, 5.38, 5.99, 6.84, 8.12, 8.89, 9.43]
y = [0.88, 2.45, 2.43, 4.07, 5.49, 6.46, 7.02, 8.27, 8.70, 10.23, 10.65]

# 一次関数の推測を行う
a, b = fit(x, y)


plt.plot(x, y, 'o')
plt.show()

# 推測した結果を基に作成したグラフを描画
y2 = [num * a + b for num in x]
plt.plot(x, y2)
plt.plot(x, y, 'o')  # 元のドットも同時に描画しておく
plt.show()
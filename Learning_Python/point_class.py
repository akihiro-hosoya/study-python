# Pointクラス
from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def difference(self, point=None):
        if not point:
            point = Point() # 原点を表すPointクラスのインスタンスを生成
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        """
        第2パラメーターにはPointクラスのインスタンスを渡すが、そのデフォルト引数値に「None」が指定されている。
        よって、differenceメソッド呼び出しで引数を指定しなかったときには、
        パラメーターpointの値はNoneになる。Noneは、値が存在しないことを意味する、
        Pythonの特殊な組み込み定数で、ブール演算を行う際には偽（False）として扱われる。

        そこで、まずはif文でパラメーターpointが偽かどうかを調べて、
        そうであれば原点(0.0, 0.0)を表すPointクラスのオブジェクトを作成することで、
        最終的には2点間の距離を求める公式を使って戻り値を計算するようにしている。
        こうすることで、原点からの距離と2点間の距離の両者を計算できるようにしている
        """

point1 = Point(1.0, 1.0)
point2 = Point()
point3 = Point(5, 4)

print(point1.difference(point2))
print(point1.difference())
print(point3.difference(point1))

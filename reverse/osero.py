import numpy as np


# オセロのマスの状態
'''
1.空きマス = 0
2.黒石が置いてある = 1
3.白石が置いてある = -1

「石を裏返す」時は　*1　をすれば良くなる
壁 = 2
'''
empty = 0
white = 1
black = -1
wall = 2

# ボードのサイズ
boardSize = 8


class Board:
    # 初期設定
    def __init__(self):

        '''
        ボードを表現する2次元配列：RawBoard
        '''
        # 全マスを空きマスに設定
        self.rawBoard = np.zeros((boardSize+2, boardSize+2)) # 全てに0を入れている

        # 壁の設定 周りに2を代入
        self.rawBoard[0, : ] = wall
        self.rawBoard[ :, 0] = wall
        self.rawBoard[boardSize+1, :] = wall
        self.rawBoard[:, boardSize+1] = wall

        # 初期配置
        self.rawBoard[4,4] = self.rawBoard[5,5] = white
        self.rawBoard[4,5] = self.rawBoard[5,4] = black

        # 手番数を表す変数:turns
        self.turns = 0

        # 現在の手番の色
        self.currentColor = black # 最初は黒から始まるから



    # 石を置く
    '''
    マスの座標（横方向）：x
    マスの座標（縦方向）：y
    '''
    def move(self, x, y):

        # 置く位置が正しいかどうかをチェック
        if x<1 or boardSize<x:
            return False
        if y<1 or boardSize<y:
            return False
        if self.movablePos[x, y] == 0: # そこに石が置けるかどうかチェック
            return False
        
        # 石を裏返す
        self.flipDiscs(x, y)

        # 手番を進める
        self.turns += 1


'''
# ボートインスタンスの作成
board = Board()
# rawBoardの中身を確認する
print(board.rawBoard)
'''

    
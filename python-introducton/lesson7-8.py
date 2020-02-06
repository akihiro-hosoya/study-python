# coding:utf-8:
import tkinter as tk

# Ballクラスの定義
class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
    #円を動かすためのメソッド
    def move(self, canvas):
        # 今の円を消す
        canvas.create_oval(self.x-21, self.y-21, self.x+21, self.y+21, fill='white', width=0)
        # x座標を動かす
        self.x = self.x + self.dx
        # y座標を動かす
        self.y = self.y + self.dy
        # 次の位置に円を描く
        canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill=self.color, width=0)
        # 端を超えたら反対向きにする
        if self.x >= canvas.winfo_width():
            self.dx = -1
        if self.x <= 0:
            self.dx = +1
        if self.y >= canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.dy = +1

# 円を作成
balls = [
    Ball(400, 300, 1, 1, 'red'),
    Ball(200, 100, -1, 1, 'green'),
    Ball(100, 200, 1, -1, 'blue')
]

def loop():
    # 動かす
    for b in balls: # ballから1つずつ取り出す
        b.move(canvas) # 動かせと命令する
    # もう1回
    root.after(10, loop)

# ウィンドウを描く
root = tk.Tk()
root.geometry('800x600')

# キャンバスを置く
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

# タイマーを設定する
root.after(10, loop)

root.mainloop()
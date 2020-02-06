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
        self.erase(canvas)
        # x座標を動かす
        self.x = self.x + self.dx
        # y座標を動かす
        self.y = self.y + self.dy
        # 次の位置に円を描く
        self.draw(canvas)
        # 端を超えたら反対向きにする
        if self.x >= canvas.winfo_width():
            self.dx = -1
        if self.x <= 0:
            self.dx = +1
        if self.y >= canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.dy = +1
    def erase(self, canvas):
        canvas.create_oval(self.x-21, self.y-21, self.x+21, self.y+21, fill='white', width=0)
    def draw(self, canvas):
        canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill=self.color, width=0)

class Rectangle(Ball):
    def erase(self, canvas):
        canvas.create_rectangle(self.x-21, self.y-21, self.x+21, self.y+21, fill='white', width=0)
    def draw(self, canvas):
        canvas.create_rectangle(self.x-20, self.y-20, self.x+20, self.y+20, fill=self.color, width=0)

class Triangle(Ball):
    def erase(self, canvas):
        canvas.create_polygon(self.x+1, self.y-21, self.x+21, self.y+21, self.x-21, self.y+21, fill='white', width=0)
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y-20, self.x+20, self.y+20, self.x-20, self.y+20, fill=self.color, width=0)

# 図形を作成
balls = [
    # 円を作成
    Ball(500, 300, 1, 1, 'red'),
    # 四角形を作成
    Rectangle(400, 300, -1, 1, 'red'),
    # 三角形を作成
    Triangle(300, 200, 1, -1, 'red')
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
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.place(x=0, y=0)

# タイマーを設定する
root.after(10, loop)

root.mainloop()
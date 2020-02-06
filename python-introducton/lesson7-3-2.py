# coding:utf-8
import tkinter as tk

# 円の座標
x = 300
y = 200

# クリック関数を作成
def click(event):
    global x, y
    #今の円を消す
    canvas.create_oval(x-21, y-21, x+21, y+21, fill='white', width=0)
    x=event.x
    y=event.y
    # クリックされたときにそこに描画する
    canvas.create_oval(event.x-20, event.y-20, event.x+20, event.y+20, fill='red', width=0)

# ウィンドウを描く
root = tk.Tk()
root.geometry('600x400')

# Canvasを置く
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.place(x=0, y=0)

# 円を描く
canvas.bind('<Button-1>', click)

root.mainloop()
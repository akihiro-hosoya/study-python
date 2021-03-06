# coding:utf-8
import tkinter as tk

# クリック関数を作成
def click(event):
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
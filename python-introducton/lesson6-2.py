#coding:utf-8

import tkinter as tk
import tkinter.messagebox as tmsg

#ボタンがクリックされたときに実行される関数を作成する
def ButtonClick():
    #テキスト入力欄の文字列を取得
    b = editbox1.get()
    # メッセージとして表示
    tmsg.showinfo('入力されたテキスト', b)

#ウィンドウを作る
root = tk.Tk() #tkinterでウィンドウを表示するときの決まり文句
#geometryメソッド
root.geometry('400x150') #ウィンドウサイズを変更する
#titleメソッド
root.title('数当てゲーム')

#Labelメソッド
label1 = tk.Label(root, text='数を入力してね', font=('Helvetica', 14)) 
#placeメソッド
label1.place(x = 20, y = 20) 
#Entryメソッド
editbox1 = tk.Entry(width = 4, font=('Helvetica', 28))
editbox1.place(x=120, y=60)

#Buttonメソッド
button1 = tk.Button(root, text ='チェック', font=('Helvetica', 14), command=ButtonClick)
button1.place(x=220, y=60)

root.mainloop() #tkinterでウィンドウを表示するときの決まり文句
# continue
# 現在のループを中断し、次の繰り返し処理を行う場合
# ここでいう「中断」は、ループそのものを中断することではなく、continue以降の処理をスキップすることを指す

# continueの基礎
for num in range(101):

    if num % 10:
        continue # 10で割り切れないものは、printを実行させずに次の繰り返し処理を行う

    print(num)
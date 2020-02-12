# if文
# 条件分岐

# 基本構文
number = input('何か数値を入力してください：')
number = int(number)

if number % 2 == 0:
    print('even')
else:
    print('odd')


# FizzBuzz問題
number = input('何か数値を入力してください：')
number = int(number)

if number % 15 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)

# 真偽値
print(7 % 2 == 0)
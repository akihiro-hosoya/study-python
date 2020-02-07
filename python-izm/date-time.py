# 日付の取得
import datetime

today = datetime.date.today()
todaydetail = datetime.datetime.today()

# Today's date
print(today)
print(todaydetail)
print('--------------------')

# 細かい値
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)
print('--------------------')

# 日付のフォーマット
print(today.isoformat())
print(todaydetail.strftime('%Y/%m/%d %H:%M:%S'))

print('----------------------------------------')
print('----------------------------------------')

# 日付の計算
today = datetime.datetime.today()

# 今日の日付
print(today)
# 明日の日付
print(today + datetime.timedelta(days=1))

newyear = datetime.datetime(2021, 1, 1)

# 2021年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))
# 2021年1月1日から今日までの日数
calc = newyear - today
# 計算結果の戻り値は「timedelta」
print(calc.days)

# 閏年の判定
import calendar

print(calendar.isleap(2015))
print(calendar.isleap(2016))
#指定期間内に何回の閏年があるか調べる
print(calendar.leapdays(2010, 2020))
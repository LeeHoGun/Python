# week5_3_datetime.py 
import datetime

now = datetime.datetime.now()

print(now.year)  # 2023
print(now.month)  # 9
print(now.day)  # 24

print(now.hour)  # 8
print(now.minute)  # 9 or 10
print(now.second)  # ??

if now.hour < 12:
    print("오전")
else:
    print("오후")

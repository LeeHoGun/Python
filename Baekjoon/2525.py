hour, minute = map(int, input().split())

plus_minute = int(input())

minute += plus_minute


if minute >= 60:
    hour += minute / 60
    minute = minute % 60

if hour >= 24:
    hour = hour % 24

print(int(hour), int(minute))




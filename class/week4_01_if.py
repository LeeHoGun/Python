# week4_01_if.py

# 주민등록번호 
reg_number = input("주민등록번호:")
gender_number = int(reg_number[6])
# 남자인지 판별하는 if문 작성하시오

if gender_number == 1 or gender_number == 3 or gender_number == 5:
    print("남자입니다.")
else:
    print("여자입니다.")

# p.122
# if gender_number in "1357":
    # print("남자")

if str(gender_number) in "1357":
    print("남자")

if reg_number[6] in "1357":
    print("남자")

if gender_number % 2 == 1:
    print("남자")

number = int(input("정수:"))

if number > 0:
    print("양수")

if number < 0:
    print("음수")

if number == 0:
    print("0")
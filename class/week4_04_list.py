# week4_03_list.py      시험 예상 문제

stu_1 = [20230001, "김인하", "컴정", 20]
stu_2 = [20230010, "이인하", "컴시", 21]

# 20230010학생의 성(family name)을 출력하세요.      중요
print("성")
print(stu_2[1][0]) # == "이인하"

# stu_1의 학생 입학년도 출력        중요
print("입학년도")
print(str(stu_1[0])[:4]) # "20230001"

print("학번")
print(stu_1[0])
print(stu_2[0])

print("이름")
print(stu_1[1])
print(stu_2[1])

stu_1[0] = 20230002
print(stu_1[0])


# list = array와 비슷한 역할
# array(배열) --> 고정길이(특징, 단점). 메모리에 연속적인 할당(장점)

test_list = list() # 생성자
print(test_list, type(test_list))

test_list = [] # 기호로 표현
print(test_list, type(test_list))

test_list = [1, 2, 3]
print(test_list)

# 다른 타입을 넣어도 됨.
test_list = ["이호건", 20, 175]
print(test_list)

for data in test_list:
    print(data)
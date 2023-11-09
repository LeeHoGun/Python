# week5_01_str.py

data1 = 41.5678900
data2 = 50.0
print(data1, data2)
print(f"{data1:.2f}")
print(f"{data2:g}")

name = input("이름:")
age = int(input("나이:"))

# 방법3: f-string p.146
data = f"{name}의 나이는 {age}살 입니다."
print(data)

# 방법2: format()메소드 이용 p.134
data = "{0}의 나이는 {1}살 입니다. {0}는 학생입니다".format(name, age)
print(data)

data = "{1}의 나이는 {0}살 입니다.".format(name, age)
print(data)

data = "{0}의 나이는 {1}살 입니다.".format(name, age)
print(data)

data = "{}의 나이는 {}살 입니다.".format(name, age)
print(data)

# 방법1: 전통적인 파이썬 동적 문자열 생성
data = "%s의 나이는 %d살 입니다." % (name, age)
print(data)

# +연산자 이용
data = "이름:" + name + " 나이:" + str(age)
print(data)

# print()로 나열한 방법
print("이름:", name, "나이:", age)

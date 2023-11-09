# week6_01_ex.py

name = input("이름:")
age = int(input("나이:"))

# 방법3 - 보건법, f-string
intro = f"이름:{name} 내년 나이:{age+1}"
print(intro)
print(end="\n\n\n")

# 방법2
intro = "이름:{1} 나이:{0}".format(name, age)
print(intro)
print(end="\n\n\n")


intro = "이름:{} 나이:{}".format(name, age)
print(intro)
print(end="\n\n\n")


# 방법1 - 전통적인 방식
intro = "이름:%s 나이:%d" % (name, age)
print(intro)
print(end="\n\n\n")
# %s: 문자열 . %d: 정수형


intro = "이름:name 나이:age"
print(intro)
print(end="\n\n\n")

print("이름:" + name + "나이:" + str(age))
# print("이름:" + name + "나이:" + age) 나이까지는 문자열이고 age는 정수 타입이라 오류가 발생함. 
# str함수를 써서 문자열로 바꿔준 후 실행해야 오류가 해결됨.


print("나의 이름은 ", name, "이고 나이는 ", age, "살 입니다.", sep="")

# " " : 공백 문자
# "" : 빈 문자열
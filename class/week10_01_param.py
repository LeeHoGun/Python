# week10_01_param.py

# p.278 가변 매개변수
# *args(가변인자)
def intro(name, grade, *hobbies):
    print(type(hobbies))
    print(name, grade)

    if 0 < len(hobbies):
        print(", ".join(hobbies))
    else:
        print(hobbies)
        print("없다")

intro("김인하", 1, "디아블로4", "카트라이더", "삼국지", "대항해시대")
intro("김인하", 1, "디아블로4")
intro("김인하", 1)


# p.280 키워드 매개변수
def intro(name, grade = 1, hobby = "없음"):
    print(f"이름:{name}")
    print(f"학년:{grade}")
    print(f"취미:{hobby}")

# intro(hobby = "게임", grade = 2) # name 지정 해야됨)
intro(hobby = "게임", name = "이호건")
intro(name = "이호건", hobby = "게임") 
intro("이호건", hobby = "게임")
intro("이호건", "없다")
intro("이호건")

# p.278 가변매개수 / p.279 기본(값) 매개변수 default argument
# 기본값 매개변수 선언은 뒤쪽에...
# def intro(grade = 1, name):
#     print(f"나는 {name}이고, {grade}학년이야")

# def intro(hobby, grade = 1, name):
#     print(f"나는 {name}이고, {grade}학년이야")

def intro(name, grade = 1):
    print(f"나는 {name}이고, {grade}학년이야")

intro("이호건")
intro("이호건", 3)

# print("이호건", end = "\t")
# print("20", "인하", "공업", sep = "\n")






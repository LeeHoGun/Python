# week5_06_dict.py

a = "string"
a[0]  # "s"

b = [1, 2, 3]
b[0]  # 1

c = {1: "one", 2: "two"}
c[1]  # "one"


infos = {
    "20230001": {"name": "kim inha", "age": 21},
    "20230002": {"name": "choi comjung", "age": 22, "major": "컴퓨터정보"},
}
print(infos["20230002"]["major"])


infos = {1: ["kim inha", 21], 2: ["choi comsung", 22]}

infos[2]  # ["choi comsung", 22] -> list
print(infos[2][1])

a = infos[2]  # ["choi comsung", 22]
b = a[0]  # "choi comsung"
c = b.split(" ")  # ["choi", "comsung"]
d = c[0]
print(d)


# p.216
info_a = {
    "name": "Kim inha",
    "age": 21,
    # height: 170 key는 지정하지 않는 변수를 쓰면 안됨
}

info_b = {"name": "choi comjunsg", "age": 22}

# print(info_a[0]) # KeyError
# print(info_a[name]) # NameError
# info_a["이름"]
print(info_a["name"])
print(info_b["age"])


test_dict = {
    "one": 1,
    # "one": 2, value은 동일해도 되지만, key는 동일한 key를 허용하지 않습니다.
    "two": 2,
    "three": 3,
}

print(test_dict)


test_dict = dict()
print(test_dict, type(test_dict))

test_dict = {}
print(test_dict, type(test_dict))

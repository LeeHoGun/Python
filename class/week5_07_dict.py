# week5_07_dict.py
infos = {
    "20230001": {"name": "kim inha", "age": 21},
    "20230002": {"name": "choi comjung", "age": 22, "major": "컴퓨터정보"},
}

infos["20230003"] = {}
infos["20230003"]["name"] = "yi comsi"
infos["20230003"]["major"] = "컴퓨터시스템"

infos["2023004"] = {"name": "wange junja", "major": "전자"}

print(infos)


test_dict = {1: "uno", 2: "two", 3: "three"}

test_dict[5] = "five"
print(test_dict)

test_dict[1] = "one"
print(test_dict)

del test_dict[2]
print(test_dict)

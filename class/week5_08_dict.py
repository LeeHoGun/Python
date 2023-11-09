# week5_08_dict.py

infos = {
    "20230001": {"name": "kim inha", "age": 21},
    "20230002": {"name": "choi comjung", "age": 22, "major": "컴퓨터정보"},
}

number = input("학번:")
# print(infos[number]) #KeyError 발생할 확률이 많음

info = infos.get(number, "학번이 없어요")
print(info)
print()

# info = infos.get(number)
# print(info) #Key가 없으면 None 반환
# print()


if number in infos:  # (원래) infos.keys()
    print(infos[number])
else:
    print("학번이 없습니다.")

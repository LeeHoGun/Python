# week5_09_dict.py
infos = {
    "20230001": {"name": "kim inha", "age": 21},
    "20230002": {"name": "choi comjung", "age": 22, "major": "컴퓨터정보"},
}

# p.256
for key, value in infos.items():
    print(key, value)
print()
print()

# p.226

for value in infos.values():
    print(value)
print()
# keys() , values()

for key in infos.keys():
    print(infos[key])
print()

for key in infos.keys():
    print(key)
print()

for key in infos:
    print(key)

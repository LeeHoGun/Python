# week5_5_for.py

# p. 207
test_list = [1, 2, 3, 20, 22]

#향상된 for문, foreach문 for-in
for element in test_list:
    print(element)

for element in "컴퓨터정보과":
    print(element)


list_of_list = [
    [1, 2, 3],
    [3, 4, 5, 7],
    [10, 11],
]

# 책에 없음
for items in list_of_list:
    for item in items:  # [1,2,3]
        print(item, end=" ")  # 1 2
    print()

print()

for items in list_of_list:
    print(items)
print()

name = "장은미"
scores = [22, 100, 30, 40]

for ele in name:
    print(ele, end="/")

for score in scores:
    print(score)

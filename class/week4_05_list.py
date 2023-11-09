# week_04_list.py

# p.146 리스트에 요소 추가하기: append, insert

test_list = [1, 2, 3]
test_list.append(5)
test_list.append(8)
print(test_list)

test_list.insert(3, 4) # insert(삽입할 위치, 삽입할 값)
print(test_list)

test_list.insert(-19, 4)
print(test_list)

test_list.insert(100, 88)
print(test_list)

str_test = "aaa"
str_test.insert(1, "b")

# print(1)
# print("1")
# print([1, 2, 3])
# print(1.1)

# print(test_list)
# test_list.pop() 
# pop함수 : 리스트의 특정 인덱스 값을 삭제 및 반환하는 기능을 갖는다.
# p.144 리스트 연산자: 연결(+), 반복(*), len()
test_list1 = [1, 2, 3]
test_list2 = [3, 4]

print(1 + 1)
print("1" + "1")
print(test_list1 + test_list2)
print(test_list2 * 3)
print(test_list1)
print(len(test_list1))
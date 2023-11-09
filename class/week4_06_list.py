# week4_05_list.py

test = ["망고", "샤인머스켓", "복숭아", "배", "사과"]

del test[4]
print(test)

del test[0:2]
print(test)

test.append("키위")
test.append("거봉")
test.append("블루베리")
print(test)

test.remove("복숭아")
print(test)

p = test.pop()
print(p)
test.pop()
test.pop(0)

print(test)

test.pop()
test.pop()
test.pop(0)
# pop함수 : 리스트의 특정 인덱스 값을 삭제 및 반환하는 기능을 갖는다.

print(test)

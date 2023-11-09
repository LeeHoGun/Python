# p.210

def test():
    print(1)
    print(2)
    return None

print(test()) # None

def test():
    print("3")
    print("4")
    return 0 # 함수를 종료하고 호출했던 곳으로 돌아감

print(test()) # 0

def test():
    print("5")
    return
    print("6")
    return 0 # 함수를 종료하고 호출했던 곳으로 돌아감

print(test()) # None

def test(n, content): # 매개변수(parameter) p.211
    for i in range(n):
        print(content)

test(2, "안녕") # 인자, argument
# 안녕
# 안녕

def avg(datas):
    if type(datas) is list:
        return sum(datas) / len(datas)

print(avg([1,2,3,4]))
result = avg("1234")
if result:
    print(result)
else:
    print("자료형에 문제가 있습니다.")

def calculate_average_from_dict(scores):
    if type(scores) is dict:
        values = list(scores.values())
        return sum(values) / len(values)

student_scores = {"김인하":92, "이인하":85, "박인하":78}
avg_score = calculate_average_from_dict(student_scores)
print(f"평균 점수:{avg_score:.2f}")

def remove_value(_list, target):
    return [i for i in _list if target != i]
    # src_list = _list[:]
    # while target in src_list:
    #     src_list.remove(target)
    # return src_list

numbers = [1,2,3,2,4,2,5]
value_remove = 2
new_numbers = remove_value(numbers, value_remove)
print(numbers, new_numbers)
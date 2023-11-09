# week5_4_list_method.py
# p.200
a = ["a", "1", 1.1]
print(1 in a)
print("1" in a)
print("A" not in a)
print("a" not in a)
print()

a = [3, 5, 7, 4, 1]
b = a[:]  # 리스트 복사

c = sorted(a)
d = sorted(a, reverse=True)
print(c)
print(d)
print(a)

a.sort()
print(a)  # asc sorting, 정방향, 오름차순
a.sort(reverse=True)  # desc sorting, 역방향, 내림차순
print(a)
print(b)
print()

a = [1, 2, 3, 4, 5]
print(a)
del a[:]  # a.clear()
print(a)

test_list = [1, 2, 3]
add_list = ["a", "b"]

# test_list.extend(add_list)
add_list.extend(test_list)
print(test_list)
print(add_list)


result_list = test_list + add_list
print(test_list + add_list)
print(result_list)
print(test_list)
print(add_list)

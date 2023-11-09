Lst = []

for i in range(10):
    num = int(input())
    remain = num % 42
    Lst.append(remain)
    Lst = list(set(Lst))

print(len(Lst))
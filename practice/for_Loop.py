# p.54

for i in range(2, 10):
    print(i, end="/")
print()

for i in range(2, 10):
    print(f"구구단:{i}단")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end="")
    print()

for d1 in data:
    for d2 in d1:
        print(d2, end=" ")
    print()

for i, d1 in enumerate(data):
    for j, d2 in enumerate(d1):
        print(f"data[{i}][{j}]={d2}", end=" ")
    print()
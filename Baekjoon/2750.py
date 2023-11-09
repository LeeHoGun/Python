num = int(input())

number = []

for _ in range(num):
    n = int(input())
    number.append(n)

print()
number.sort()

for i in number:
    print(i)
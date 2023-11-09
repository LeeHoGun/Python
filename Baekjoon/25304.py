Price = int(input())
number = int(input())

sum = 0

for i in range(number):
    A, B = map(int, input().split())
    sum += A * B

if Price == sum:
    print("Yes")
else:
    print("No")
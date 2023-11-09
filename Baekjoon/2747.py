n = int(input())

A, B = 0, 1

for i in range(n):
    A,B = B, A+B

print(A)
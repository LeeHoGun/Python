A = int(input())
B = int(input())
C = int(input())

M = A * B * C  # multiplication

Number = list(map(int, str(M)))

print(Number)

for i in range(10):
    print(Number.count(i))


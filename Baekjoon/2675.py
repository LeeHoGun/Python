S_num = int(input())

for _ in range(S_num):
    [num,word] = input().split()
    for i in word:
        print(i * int(num), end = '')
    print()
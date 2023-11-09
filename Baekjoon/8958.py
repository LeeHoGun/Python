n = int(input())

for _ in range(n):
    score = 0
    result = 0
    Figure = input()
    for i in Figure:
        if i == "O":
            score += 1
        else:
            score = 0
        result += score
    print(result)
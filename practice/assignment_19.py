def avg_score(scores):
    if type(scores) is dict:
        values = list(scores.values())
        return sum(values) // len(values)

scores = {"kim": 95, "lee": 65}
avg = avg_score(scores)

if avg != None:
    print(f"평균: {avg}")
else:
    print("점수가 없음")

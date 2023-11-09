# p.55

students = [] # n명의 학생의 3과목 점수
titles = ["국어", "영어", "수학"]

number = int(input("인원:"))

for i in range(number):
    print(f"{i+1}번 학생>>")
    scores = []
    for title in titles:
        score = input(f"{title} 과목:")
        scores.append(int(score))
    students.append(scores)

# for i, scores in enumerate(students):
#     print(f"{i+1}번 학생:")
#     for j, score in enumerate(scores):
#         print(f"\t{titles[j]}:{score:>3}")               
#     print(f"\t평균:{sum(scores) // len(scores):>3}")

for i in range(len(students)):
    print(f"{i + 1}번 학생:")
    scores = students[i]  # 현재 학생의 점수
    for j in range(len(scores)):
        print(f"\t{titles[j]}:{scores[j]:>3}") 
    average = sum(scores) // len(scores)  # 평균값 계산
    print(f"\t평균:{average:>3}")
    # :3 --> 공백 추가 ex) 평균:18 --> 평균:  18
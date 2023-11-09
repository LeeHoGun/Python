def get_students(scores):
    if not scores:
        return []  
    
    elif type(scores) is dict:
        student_list = list(scores.keys())  
        return student_list

scores = {"kim": 95, "lee": 65}
students = get_students(scores)

if students:
    students = ",".join(students)
    print(f"명단:{students}")
else:
    print("학생이 없음")

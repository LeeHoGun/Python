def add_dict(l1st, K_name, value_score) :
  for i in l1st:
    if i == K_name :
      return False
  l1st[K_name] = value_score
  return True
  
scores = {"kim":95, "lee":65}

if add_dict(scores, "park", 100) :
  print("입력 완료")
  # print(scores)
else:
  print("동일 학생 있음")
  

if add_dict(scores, "kim", 100) :
  print("입력 완료")
  # print(scores)
else:
  print("동일 학생 있음")
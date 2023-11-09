def add_list(l1st_A, l1st_B):
  L1st = []
  
  if len(l1st_A) > len(l1st_B):
    dif = len(l1st_A)-len(l1st_B)
    for i in range(dif):
      l1st_B.append(0)
    
  else:
    dif = len(l1st_B)-len(l1st_A)
    for i in range(dif):
      l1st_A.append(0)
  
  for i in range(len(l1st_A)):
    L1st.append(l1st_A[i]+l1st_B[i])
  return L1st

print(add_list([1,2,3,4],[1,2]))
print(add_list([0,1],[1,2,6,7,8]))

def merge_list(list1, list2):
    l1st = list(set(list1 + list2)) 
    l1st.sort()  
    return l1st

result1 = merge_list([1, 2, 3, 4], [1, 2, 5])
print(result1)  

result2 = merge_list([0, 1, 10], [1, 2, 6, 7, 8])
print(result2)  

def search_index(input_list, target):
    index_num = [i for i, value in enumerate(input_list) if value == target]
    return index_num

result1 = search_index([35, 28, 30, 29, 30], 30)
print(result1)  

result2 = search_index([35, 28, 30, 29, 30], 31)
print(result2)  

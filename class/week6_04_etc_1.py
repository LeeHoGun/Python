# week6_04_etc_1.py
# 연습문제
ip_addr = [127, 0, 0, 1] # 127.0.0.1
ip_addr_neu = [str(ip) for ip in ip_addr]
ip_addr_neu = ".".join(ip_addr_neu)
print(ip_addr_neu)

# p.198 리스트 내포(List comprehension)
array = []
for i in range(0, 20, 2):
    if i % 4:
        array.append(i * i)
print(array)
print()

array = [i * i for i in range(0,20,2) if i % 4] # 3 1 2 순서로 보면 됨 

array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
print()

array = [i * i for i in range(0,20,2)]

# p.203 - join()

fruits = ["딸기", "사과", "배"]

print(",".join(fruits)) # 딸기,사과,배

my_fav = ""
for f in fruits:
    if len(my_fav) > 0: 
        my_fav += ","
    my_fav += f
print(my_fav) # 딸기,사과,배

# p.196 -items() dict메소드...
example = {1: "one", 2: "two", 5: "five"}

for k in example: # 1 2 5
    print(k)

for k in example.keys(): # 1 2 5
    print(k)

for v in example.values(): # one two five
    print(v)

for k, v in example.items():
    print(k, v)

# p.194
# enumerate()의 결과는 tuple의 형태
scores = [100, 45, 80, 0, 23]
for i, score in enumerate("이호건"):
    print(f"{i+1}번 과목:{score}")


for i, score in enumerate(scores):
    print(f"{i+1}번 과목:{score}")

# p.192
scores = [100, 45, 80, 0, 23]
print(reversed(scores))
print(list(reversed(scores)))
print(scores)
for r in reversed(scores):
    print(r)

a = reversed(scores)
for r in a:
    print("1st", r)
for r in a:
    print("2nd", r)
    
print("\n\n\n\n")

# p.190
scores = [100, 45, 80, 0, 23]

print(min(scores))
print(max(scores))
print(sum(scores))
print(sum(scores)/len(scores))

# 사용자가 입력한 점수를 가지고 평균을 구하는 코드를 짜시오.

#방법1 
print(sum(scores)/len(scores))
# scores 합계 / scores의 길이 

#방법2

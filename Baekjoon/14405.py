list = ["pi", "ka", "chu"]

s1 = input()

for i in list:
    s1 = s1.replace(i, " ")

print(s1)

if len(s1.strip()) == 0:
    print("YES")
else:
    print("NO")
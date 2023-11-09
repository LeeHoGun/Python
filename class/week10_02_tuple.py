# p.317

tuple_data = (10, 20, 30)

a = tuple_data[0]
b = tuple_data[0:]

print(a, b, list(b))

tuple_data = (10, 20, 30)

for i, v in enumerate(tuple_data):
    print(i, v)

# p.318

a = []
b = [1]
c = ()
d = (1, ) #cf. d = (1) | [튜플] 데이터가 하나만 들어갈 경우에는 반드시 뒤에 ,(콤마) 기입. 또한 괄호() 생략 가능

print(type(a), type(b), type(c), type(d))

# p.318
a, b = [10, 20]
c, d = (10, 20)
print(a, b, c, d)

a = (10, 20, 30)
b, c, d = a

a = 10, 20, 30
b, c, d = a
print(a,b,c,d)

# p.320
a,b = 10, 20
b, a = a, b

for i in enumerate([1,2,3]):
    print(a[0], b[1])

for i, v in enumerate([1,2,3]):
    print(i, v)

def divide(n1, n2):
    a = n1 // n2
    b = n1 % n2
    return a, b

q, r = divide(10, 3)
print(q, r)
def call_10_times(func):
    for i in range(10):
        func(i)

def print_hello(i):
    print(f"{i+1} 안녕")

def print_bye(i):
    print(f"{i+1} 꺼져")

call_10_times(print_hello)
print()
call_10_times(print_bye)

# p.323 map()
a = ["1", "2", "3"]
# a = [int(i) for i in a]
a = list(map(int, a))
b = sum(a)

def power(item):
    return item ** 2

a = [1, 2, 3]
b = list(map(power, a))

print(b)

a = [1, 2, 3]
b = list(map(lambda x : x ** 2, a))
print(b)

def under_3(item):
    return item < 3

list_data_a = [1, 2, 3, 4, 5]

output_data = filter(under_3, list_data_a)
print(output_data, list(output_data))

output_data = filter(lambda x : x < 3, list_data_a)
print(output_data, list(output_data))
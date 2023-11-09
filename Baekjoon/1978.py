#소수를 판단하는 함수 is_prime
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
    return True
N = int(input())
nums = list(map(int,input().split()))
cnt = 0
for i in nums:
    if isPrime(i):
        cnt += 1
print(cnt)

# def is_sosu(inp):
#     for i in range(2, inp):
#         if inp % i != 0:
#             pass
#         else:
#             return 0
#     return 1

# N = int(input())
# num = list(map(int,input().split()))

# result = 0

# for i in num:
#     n = is_sosu(i)
#     print(n)
#     if n == 1:
#         result += 1

# print(result) 




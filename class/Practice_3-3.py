money = int(input("투입한 돈:"))
price = int(input("물건의 가격:"))

change = money - price
print("거스름 돈:", change)

coin500 = change // 500 # 500으로 나눠서 몫이 500원짜리 개수
change = change % 500 # 500으로 나눈 나머지 계산

coin100 = change // 100 
change = change % 100

print("500 동전 개수:", coin500)
print("100 동전 개수:", coin100)

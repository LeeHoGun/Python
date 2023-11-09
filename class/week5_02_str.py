# week5_02_str.py
b = "10 20-30 40-50,60"

print("10" in b)
print("11" in b)
print("12" not in b)


b = "10 20-30 40-50,60"
# c = b.split()
c = b.split(" ")
print(c)

c = b.split("-")
print(c)

c = b.split("$")
print(c)

print("=" * 30)

a = "     hello PYthone!   "
print(a.find("o"))
print(a.find("O"))  # 찾지 못하는 경우 -1
print(a.rfind("o"))
print()

print(f"[{a.strip()}]") # 중요
print(f"[{a.lstrip()}]")
print(f"[{a.rstrip()}]")
print()


print(a.upper())  # "     HELLO PYTHONE!   " # 중요
print(a.lower())  # "     hello pythone!   " # 중요
print(a.title())  # "     Hello Pythone!   "
print(a)
print()

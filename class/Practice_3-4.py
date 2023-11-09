symbols = input("기호:")
text = input("삽입 문자열:")

print("출력:", symbols[:1] + text + symbols[-1]) # +index ->  0 1 2 ~~ / -index -> -3 -2 -1 ~~
# 2) 집합 자료형
print("1. 문자열: ", "hello")
print("1. 문자열: ", 'hello')
print("1. 문자열: ", """hello""") # triple
print("1. 문자열: ", '''hello''')

print("2. 리스트(list): ", [1, 2, 3, 4, 4, "hello"])
print("3. 셋(set): ", {1, 2, 3, 4, 4, "hello"})
print("4. 튜플(tuple): ", (1, 2, 3, 4, 4, "hello"))
print("5. 딕트(dict): ", {"name": "홍길동", "age": 20})

# 이스케이프 문자 (escape 문자)
print("c:\\temp")
print("Hello\nworld")
print("Hello\tworld")
print("she\s'")
print("\"hello\"")

# raw string # 스케이프 문자를 무시한다.
#
print(r"c:\\temp") # c:\\temp
print(r"Hello\nworld") # Hello\nworld
print(r"Hello\tworld")  # Hello\tworld
print(r"she\s'") # she\s'
print(r"\"hello\"") # \"hello\"

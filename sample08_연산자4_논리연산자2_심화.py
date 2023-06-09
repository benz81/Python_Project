# 논리 연산자 심화

# False로 처리되는 데이터 (외우기)
print(not 0)
print(not "")
print(not None)
print(not [])
print(not {})
print(not set(), set()) # 비어있는 셋


# True로 처리되는 데이터
print(not 10)
print(not "AA")
print(not [1,2])
print(not {"age":20})


print("공백문자:", not "" ) # True
print("0 문자:", not 0 )   # True
print("None:", not None ) # True
print("[]:", not [] )     # True
print("():", not () )     # True
print("{}:", not {} )     # True
print()
print("일반문자:", not "Hello" )  # False
print("10 문자:", not 10 )       # False


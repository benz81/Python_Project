'''
    generator 함수

    - 함수내의 문장을 단계적으로 실행 가능
    - next() 함수 이용
'''
# 1. 일반 함수
def fun():
    print("1")
    print("2")
    print("3")

f=fun()
print(f, type(f))
print("-"*100)

# 2. generator 함수

def fun():
    print("1")
    yield
    print("2")
    print("3")

f2=fun()
print(f2, type(f2))
next(f2)
next(f2)
next(f2)
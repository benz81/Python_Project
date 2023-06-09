'''
   generator Comprehension
   1) 문법:
       변수 = (표현식  for 변수 in  집합형 )
  2) 한번에 실행 안되고 단계적으로 동작 됨.
     - next() 함수 이용해서 단계적으로 값을 얻는다.
'''

list_x = [n for n in [1,2,3]]
generator_x = (n for n in [1,2,3])

print("list comprehension:" , list_x) # [1, 2, 3]
print("generator comprehension:" , generator_x) # <generator object <genexpr> at 0x0000021B6B2F8B30>

print(next(generator_x))
print(next(generator_x))
print(next(generator_x))

#실습 다음문자열에서 영문자만 뽑아서 리스트로 출력하시오
xxx = "abde1234AbCde24Dgdd22"

def fun(n):
    return n.isalpha()

result= filter(fun, xxx)
result= filter(lambda n:n.isalpha(), xxx)
# print(list(result)) # generator 객체이기 때문에 이 시점에서 모두 소비
# abde1234AbCde24Dgdd 모두 출력하시오

xxx = list(result)
print(xxx)
print("".join(xxx)) # 기억하기

# map 함수 ==> 내장된 함수에서 다른 함수적용(가공)후 반환
# 동등비교
'''
 a == b : a와 b의 실제값을 비교한다.
 a is b : a와 b의 주고삾을 비교한다.
         id(a) == id(b) 동일
'''

a = [1, 2, 3, 4, 5 ]
b = a
print(a, id(a)) # [1, 2, 3, 4, 5] 140577233330752
print(b, id(b)) # [1, 2, 3, 4, 5] 140577233330752
print( a==b)
print( a is b, id(a) == id(b))

c = a[:]  # a 복사본 생성
print(c, id(c)) # [1, 2, 3, 4, 5] 140423017481408
print(a==c)     # True
print( a is c)  # False

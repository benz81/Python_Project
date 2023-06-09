# 3) 변수 타입 체크
#일반형
a = 10
b = 3.14
c = True
x = None
y = lambda : print("hello") # 함수 <class 'function'>

# 집합형
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g = {'key': 100}
h = "hello"     # unicode string
h2 = b"hello"   # byte string ==> 웹에서 문자영을 가져올때 (크롤링)

print(a, type(a)) # 10 <class 'int'>
print(b, type(b)) # 3.14 <class 'float'>
print(c, type(c)) # True <class 'bool'>
print(x, type(y)) # None <class 'function'>
print(y, type(y)) # <function <lambda> at 0x7fdb18153af0> <class 'function'>

print(d, type(d)) # [10, 20, 30] <class 'list'>
print(e, type(e)) # (10, 20, 30) <class 'tuple'>
print(f, type(f)) # {10, 20, 30} <class 'set'>
print(g, type(g)) # {'key': 100} <class 'dict'>
print(h, type(h)) # hello <class 'str'>
print(h2, type(h2)) # b'hello' <class 'bytes'>
print(None, type(None)) # None <class 'NoneType'>

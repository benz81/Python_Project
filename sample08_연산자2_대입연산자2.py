# 대입 연산자 심화
a = b = c = 1
print(a, b, c)

name, age, address = "홍길동",20,"서울" # 중요함 , 갯수가 반드시 일치해야 한다.
print(name,age,address)       # 홍길동 20 서울

# 갯수가 달라도 된다. packing

x = [10, 20, 30]
print(x)                  # [10, 20, 30]

x, y, z = [10, 20, 30]
print(x,y,z)              # 10 20 30

x, *y = [10, 20, 30]
print(x,y)                # 10 [20, 30]

x, *y = (10, 20, 30)
print(x,y)                # 10 [20, 30]

x, *y = {10, 20, 30}
print(x,y)                # 10 [20, 30]

# dict는 key 값이 저장된다.
a, *b = {"x":"홍길동", "y":"이순신", "z":"dbrhkstns"} # 변수에 키 값이 저장
print(a, b)                     # x ['y', 'z']





v1, *v2 = [10,20,30]
print(v1,v2)  # 10 [20, 30]

v1,*v2={'a':100,'b':200 ,'c':300}
print(v1,v2)  # a ['b', 'c']

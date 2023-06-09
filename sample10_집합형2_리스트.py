#1. 리스트

# 리스트에 어떤 함수가 있는지 확인하기
print(dir(list))
'''
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
'pop', 'remove', 'reverse', 'sort']

'''

# 1)리스트 생성
string_list = ['abc', 'defghi']
int_list = [1, 2, 3, 4]
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
xxx = list('hello') # ['h', 'e', 'l', 'l', 'o']
xxx2 = list((10,20,30)) # [10, 20, 30]

print(int_list)
print(empty_list)
print(int_list*2) # 반복출력
print(xxx, xxx2)

# 2) 리스트 추가,삽입,병합,삭제
m = [1,2,3]
m.append(10)
m.append([9,8])
m.append((100,200))
print("1. append:",m) #[1, 2, 3, 10, [9, 8], (100, 200)]

# 삽입
m.insert(0,100)
m.insert(0,[4,5,6])
print("2. insert:",m) # [[4, 5, 6], 100, 1, 2, 3, 10, [9, 8], (100, 200)]

# 병합 ( extend 또는  + )
# 병합은 기본적으로
x = [1,2,3]
x.extend([10])
x.extend([9,8])
#x.extend(100) # 일반형 데이터이기 때문에 에러발생
x.extend("XYZ")
x.extend((7,))  # tuple
print("3. extend:",x) # [1, 2, 3, 10, 9, 8, 'X', 'Y', 'Z', 7]

k = (10)
k2 = (10,)
print(type(k),type(k2))  #<class 'int'> <class 'tuple'>

# 리스트 삭제
kk4 = [1,2,3,4]




kk4.pop()  # pop(-1) 과 동일
kk4.pop(0)
print("9. pop 함수(위치)",kk4)

#help(rr4.pop)
print()
kk4.remove(2)  # 값에 의한 삭제
print("10. remove(값): ", kk4)
del kk4[0]  # 위치에 의한 삭제
print("11. del(위치)", kk4)
kk4.clear()
print("12. clear: " , kk4)

# etc
print("4. 리스트 길이:" , len([1,2,3,4]))
print("5. 포함 갯수:" , [10,2,3,2,9,2].count(2))
x3 = [100,200,300]
print("6. 특정 위치:" , x3.index(200))
print("7. 포함 여부1:" , 9 in [9,8,7])
print("7. 포함 여부2:" , 6 in [9,8,7])

x = [1,2,3]
x.reverse()
print("8. 거꾸로(자신이 변경):" , x)  # [3, 2, 1]
print()
y = reversed(x)  # 뒤집힌 새로운 객체 반환
print("8. 거꾸로(새로운 객체반환):", x, list(y))  # [3, 2, 1] [1, 2, 3]

# 3) 리스트 정렬1- sort 함수
xxx = [88,2,5,3,9,7,10]
xxx.sort()
print("13. 오름차순 정렬:",  xxx)
xxx.sort(reverse=True)       #역순으로 정렬
print("13. 내림차순 정렬:",  xxx)
#help(xxx.sort)

# 3) 리스트 정렬2- sorted 함수
zzz = [3,1,2,4,5]
zzz2 = sorted(zzz)
zzz3 = sorted(zzz,reverse=True)
print("15. 정렬전:",  zzz )
print("15. 정렬후 1:",  zzz2 )
print("15. 정렬후 2:",  zzz3 )
print("15. 원본 정렬후:",  zzz)

yyy = ['123', '9999', '43']
yyy.sort()
print("14. 기본 문자열 정렬:",  yyy)

yyy.sort(key=int)
print("14. 문자형을 수치형으로 변환하여  정렬:",  yyy)  #문자열이지만 숫자형으로 정렬

zz = ['홍길동','김', '박혁거세']
zz.sort(key=len, reverse=True)
print("14. 길이에 따라서  정렬:",  zz)  # ['김', '홍길동', '박혁거세']


# 4) 리스트 인덱싱과 슬라이싱
# 1차원 리스트
arr = [1,2,3,4,5,6,7,8,9,10]
print("맨 마지막: ", arr[-1])     # 10
print("맨 마지막에서 두번째 : ", arr[-2])     # 9

print("original: ", arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("all: ", arr[:])    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("reverse: ", arr[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("1 부터 끝까지: ", arr[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("0 부터 5까지: ", arr[:6])   # [1, 2, 3, 4, 5, 6]
print("2 부터 5까지: ", arr[2:6])  # [3, 4, 5, 6]


# 2차원 리스트
arr = [[1,2,3,4,5], [10,20,30,40,50]]
print("original: ", arr)
print("all: ", arr[:])
print("arr[0]: ", arr[0]) # [1, 2, 3, 4, 5]
print("arr[1]: ", arr[1]) # [10, 20, 30, 40, 50]
print("arr[0][:3] ", arr[0][:3] ) # [1, 2, 3]
# 50 얻기
x = arr[1]
y = x[-1]
print(y)
print(arr[1][-1])

'''

      깊은 복사 : 실제값 복사
      얕은 복사 : 주소값 복사
'''

n = [1,2,3]
 #얕은 복사: 주소값 복사
m = n
print(n, id(n)) # [1, 2, 3] 140479120555904
print(m, id(m)) # [1, 2, 3] 140479120555904
n[0] = 100
print(n, m)

 #깊은 복사: 실제값 복사, 원본 변경시 복사본은 영향을 안 받는다.
n = [1,2,3]
# m=n[:]
# m=n.copy()
m =list(n)
print(n, id(n)) # [1, 2, 3] 140479120555328
print(m, id(m)) # [1, 2, 3] 140479120118464
n[0] = 100
print(n, m)
### 집합형 데이터

#1. 문자열 함수
s = 'sequence'
s = '''sequence'''
s = """sequence"""
s = str(10)

s = "sequence"
print(dir(str))
print(dir(s))

# triple 사용용도 : 정형화된 문자열 처리
s2 = """
   <html>
     <body>
       <p>
"""
print(s2)
s2 = "<html>"\
     "<body>"\
     "<p>"

#2. 문자열 함수
# 문자열은 str객체가 관리하다.
s = "sequence"

print("1. 문자열 길이:", len(s)) # 8
print("2. 특정문자 포함횟수:", s.count('e')) # 3
print("3. 소문자로:", "HeLLo".lower()) # hello
print("4. 대문자로:", "HeLLo".upper()) # HELLO
print("5. swap 문자로:", "HeLLo".swapcase()) # hEllO

print("6. 공백제거:\n")
print("    HeLLo    ".lstrip()) #
print("HHeLLH".lstrip("H")) # eLLH
print(len("    HeLLo    ".lstrip())) # 9
print("    HeLLo    ".rstrip()) #
print("HHeLLHH".rstrip("H")) # HHeLL
print("    HeLLo    ".strip()) #
print("HHeLLHH".strip("H")) # eLL
print(len("    HeLLo    ".strip())) # 5

print("7. 문자열 변경:", "HeLHO".replace('H', 'A')) # AeLAO
print("8. 구분자:", "aaa/bbb/ccc".split("/")) # ['aaa', 'bbb', 'ccc']
print("8. 구분자:", "aaa,bbb,ccc".split(",")) # ['aaa', 'bbb', 'ccc']

print('9. 특정 글자 시작 : ', s.startswith('s'), s.startswith('a')) # True False
print('10. 특정 글자 끝 : ', s.endswith('e'), s.endswith('x')) # True False

print("11. 문자로만 구성?", "대한Heloo".isalpha())  # True
print("11. 문자로만 구성?", "12".isalpha())   # False
print("11. 숫자로만 구성?", "12".isnumeric())   # True

print("12. S.find(sub[, start[, end]]) -> int")
print("12. 검색위치1:", s.find('e')) # 1
print("12. 검색위치2:", s.find('e', 2)) # 4
print("12. 검색위치3:", s.rfind('e')) # 7
help(str.find)
help(str.startswith)
help(str.rfind)

print("13. join:", ",".join(["A", "B", "C"])) # A,B,C 중요
print("13. join:", "와".join(["A", "B", "C"])) # join: A와B와C

print("14. center:", "Hello".center(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("15. rjust:", "Hello".rjust(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("16. ljust:", "Hello".ljust(20, "_")) # 20 자리수로 표시하고 _로 마킹
print("17. capitalize:", "heLLOX".capitalize()) # 첫글자 대문자

print("18. 멤버쉽 연산자1:", "H" in "Hello") # True
print("19. 멤버쉽 연산자2:", "X" in "Hello") # False

# 문자열 종류
'''
s="hello" ==> unicode string, 일반적으로 사용하는 문자열
s2=b"hello" ==> bytes string, 네트워크 이용한 경우에는 bytes string 으로 처리된다.

'''

#1) unicode --> bytes       ( 암호화 작업: encode 함수 )
#help(str.encode)
s = "hello안녕하세요"
s2  = s.encode('utf-8')
print(s, s2)

#2) bytes --> unicode        ( 암호화 작업: encode 함수 )
#print(dir(bytes))
'''
'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 
'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill']
'''

s3 = s2.decode("utf-8")
print(s2, s3)

# 2. 문자열 인덱싱과 슬라이싱
m = "대한민국"
'''
       -4 -3 -2 -1
       대  한 민  극
       0  1  2  3

'''

# 1) 인덱싱(indexing) 하나만 찍어서 가져옴
print("1:", m[0])  #  대
print("2:", m[-1]) #  국

# 2) 슬라이싱 - 범위 지정 여러 데이터 가져옴
'''
  m[start:end:step]

  start: 시작idx 값, 생략하면 맨처음
  end : 끝 idx 값, end값은 포함안됨. 생략하면 맨끝
  step: 기본값 1
'''
'''
    -4 -3 -2 -1
    대 한 민 국
    0  1  2  3 
 '''
print("3:", m[0:3]) # 대한민 - end 값은 값에 포함이 안됨 국 생략
print("4:", m[1:]) # 한민국 -  end 값 생략하면 맨끝까지 포함해서 출력
print("5:", m[:2]) #  대한 -  시작 값 생략하면 맨 처음부터 출력
print("6:", m[-3:-1]) # 한민
print("7:", m[-3:]) #  한민국
print("7:", m[:-1]) #  대한민
print("8:", m[0:3:2]) #대민
print("9:", m[:])   #대한민국
print("10:", m*2)    #대한민국대한민국
print("11:", m[::-1])    # 국민한대
print("11:", m[::-2])    # 국한

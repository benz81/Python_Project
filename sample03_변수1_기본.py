### 변수 ###

# 1) 기본
num = 4
name = "홍길동"
address = "서울"
height = 174.2
isMarried = True
email =["aa@daum.net","bb@google.com"]
info ={
    "핸드폰":["010", "011"],
    "애완동물":["강아지","고양이"]
}
print(num,id(num)) # 4 4514560752
print(name,id(name)) # 홍길동 140476167533840
print(address,id(address)) # 서울 140476167533936
print(height,id(height)) # 174.2 140476435833328
print(isMarried,id(isMarried)) # True 4514340760
print(email,id(email)) # 'aa@daum.net', 'bb@google.com'] 140476166988288
print(info,id(info)) # {'핸드폰': ['010', '011'], '애완동물': ['강아지', '고양이']} 140476166921856
'''

       range 함수

       range(stop)
       range(start,, stop[, step])
           --> start 포함, stop 미포함
           --> 기본값은 0 부터 인덱스

'''
print(range)
print(list(range(10)))  # 0~9 까지 만들어준다. 시작값을 입력하지 않았기 때문에 0부터 시작하며 10은 미포함임으로 9까지 나온다
print(list(range(1,5)))  # [1, 2, 3, 4]
print(list(range(1,10,2)))  # [1, 2, 3, 4]  1부터 10까지 2씩 증가
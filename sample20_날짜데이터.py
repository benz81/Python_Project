


from datetime import  datetime

print("1. 현재날짜", datetime.now())
print("1. 현재날짜", datetime.today())

print("2. 년도", datetime.today().year)
print("2. 월", datetime.today().month)
print("2. 일", datetime.today().day)
print("2. 시간", datetime.today().hour)
print("2. 분", datetime.today().minute)
print("2. 초", datetime.today().second)


new_date = datetime(2022,5,19)
new_date = datetime(year=2022, month=5, day=19)
new_date = datetime(year=2022, month=5, day=19, hour=12, minute=20)
print(new_date)


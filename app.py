hours,  minutes = map(int, input("시작 시간을 설정하세요 (시 분) : ").split())
add_minutes = int(input("추가할 시간을 입력해주세요 (분): "))
minutes += add_minutes

while minutes >= 60 :
    hours += 1
    minutes -= 60

if hours > 24 :
    hours %= 24
    minutes %= 60
    print("다음 날 %d시 %d분입니다." % (hours, minutes))

if "if the time is less than or equal to 24":
    hours = hours % 24 
    minutes = minutes % 60
    print("%d시 %d분입니다." % (hours, minutes))

else:
    print("Now, you can memorize this number.\n%.f", 3.141592)
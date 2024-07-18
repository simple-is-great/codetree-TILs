Y, M, D = map(int, input().split())

# 윤년 판정
def isLeapYear(year):
    result = False # 기본 -> 윤년 X
    if year % 4 == 0: # 4의 배수 -> 윤년
        result = True
        if year % 100 == 0: # 4의 배수 and 100의 배수 -> 윤년 X
            result = False 
            if year % 400 == 0: # 4의 배수 and 100의 배수 and 400의 배수 -> 윤년
                result = True
    return result

def returnSeason(year, month, day):
    if (not isLeapYear(year) and month == 2 and day == 29): # 윤년이 아닌데, 29일 -> 오류
        return -1
    else:
        if (month >= 3 and month <= 5):
            return "Spring"
        elif (month >= 6 and month <= 8):
            return "Summer"
        elif (month >= 9 and month <= 11):
            return "Autumn"
        elif (month == 12 or month == 1 or month == 2):
            return "Winter"
            
print(returnSeason(Y, M, D))
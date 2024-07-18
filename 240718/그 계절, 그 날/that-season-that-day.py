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
    # 예외 경우 더 있음, 30일인지, 31일인지 체크
    smallMonth = [2, 4, 6, 9, 11]
    if month in smallMonth and day == 31: # 작은 달인데 31일 있음
        return -1
    else:
        if (month >= 3 and month <= 5):
            return "Spring"
        elif (month >= 6 and month <= 8):
            return "Summer"
        elif (month >= 9 and month <= 11):
            return "Fall"
        elif (month == 12 or month == 1 or month == 2):
            return "Winter"
            
print(returnSeason(Y, M, D))
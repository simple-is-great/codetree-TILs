# N 주어짐, 1 ~ N까지 합을 10으로 나눈 값을 반환하는 함수, 나머지는 버리고 몫만 출력
def sum_divide_by_10(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i
    
    return sum_ // 10


N = int(input())
print(sum_divide_by_10(N))
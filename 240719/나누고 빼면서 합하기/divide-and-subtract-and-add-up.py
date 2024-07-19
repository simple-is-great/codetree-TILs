n, m = map(int, input().split())
A = list(map(int, input().split()))
sum_ = 0

def modifyIndex(): # 수열이라 인덱스가 1부터 시작함에 주의
    # 4 -> 2 -> 1
    # 지금은 2 -> 1 순으로 실행
    global m, A, sum_
    if m == 1:
        return

    if m % 2 == 1:
        m -= 1
        sum_ += A[m - 1]
    else:
        m //= 2
        sum_ += A[m - 1]
    
    modifyIndex()

sum_ += A[m-1]
modifyIndex()
print(sum_)
n, m = map(int, input().split())
A = list(map(int, input().split()))
sum_ = 0

def modifyIndex(M): 
    # 수열이라 인덱스가 1부터 시작함에 주의
    # 4 -> 2 -> 1, 지금은 2 -> 1 순으로 실행
    global A, sum_

    if M == 1:
        return

    if M % 2 == 1:
        M -= 1
        sum_ += A[M - 1]
    else:
        M //= 2
        sum_ += A[M - 1]
    
    modifyIndex(M)

sum_ += A[m - 1]
modifyIndex(m)
print(sum_)
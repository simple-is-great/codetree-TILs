n, m = map(int, input().split())
A = list(map(int, input().split())) # 수열
answer = [0] * m
for i in range(m):
    sum_ = 0
    a1, a2 = map(int, input().split())
    for j in range(a1 - 1, a2): # 수열이라 인덱스가 1부터 시작함에 주의
        sum_ += A[j]
    answer[i] = sum_

for num in answer:
    print(num)
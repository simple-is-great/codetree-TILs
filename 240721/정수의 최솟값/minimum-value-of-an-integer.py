def find_min(m, n, l):
    if m <= n and m <= l:
        return m
    elif n <= m and n <= l:
        return n
    elif l <= m and l <= n:
        return l

a, b, c = tuple(map(int, input().split()))
print(find_min(a, b, c))
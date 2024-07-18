a, b = map(int, input().split())

def modifyNumbers(n, m):
    if n >= m:
        return n * 2, m + 10
    else:
        return n + 10, m * 2

a, b = modifyNumbers(a, b)
print(a, b)
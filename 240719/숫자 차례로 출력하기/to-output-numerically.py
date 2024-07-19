N = int(input())

def recurPrintRight(n):
    if n == 0:
        return

    print(n, end = ' ')
    recurPrintRight(n-1)

def recurPrintLeft(n):
    if n == N + 1:
        return
    
    print(n, end = ' ')
    recurPrintLeft(n + 1)
    

recurPrintLeft(1)
print()
recurPrintRight(N)
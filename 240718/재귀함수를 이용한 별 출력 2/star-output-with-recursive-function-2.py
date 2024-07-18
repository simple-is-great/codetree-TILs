n = int(input())

def recurSmaller(num):
    if num == 1:
        print('*')
    else:
        print(" ".join(['*'] * num))
        recurSmaller(num - 1)

def recurLarger(num):
    if num == n:
        print(" ".join(['*'] * n))
    else:
        print(" ".join(['*'] * num))
        recurLarger(num + 1)

recurSmaller(n)
recurLarger(1)
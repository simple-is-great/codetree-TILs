def lcm(a, b):
    return int(a * b / gcd(a, b))

# 12, 18
def gcd(a, b):
    if b == 0:
        return a
    if a >= b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

n, m = map(int, input().split())

print(lcm(n, m))
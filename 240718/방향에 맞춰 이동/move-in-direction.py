N = int(input())

# N: [0, 1], E: [1, 0], S: [0, -1], W: [-1, 0]
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(N):
    dir_, amount = input().split() 
    if dir_ == 'N':
        x, y = x + int(amount) * dx[0], y + int(amount) * dy[0]
    elif dir_ == 'E':
        x, y = x + int(amount) * dx[1], y + int(amount) * dy[1]
    elif dir_ == 'S':
        x, y = x + int(amount) * dx[2], y + int(amount) * dy[2]
    elif dir_ == 'W':
        x, y = x + int(amount) * dx[3], y + int(amount) * dy[3]

print(x, y)
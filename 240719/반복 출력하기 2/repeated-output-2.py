def hello_world(n):
    if n == 0:
        return
    
    hello_world(n-1)
    print("HelloWorld")


N = int(input())
hello_world(N)
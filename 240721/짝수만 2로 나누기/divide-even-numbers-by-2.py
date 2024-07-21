def divide_even_by_two(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2


N = int(input())
numbers = list(map(int, input().split()))

divide_even_by_two(numbers)
for n in numbers:
    print(n, end = ' ')
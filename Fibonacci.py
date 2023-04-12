def fibonacci(n):
    if n <= 1: return n
    else: return fibonacci(n - 1) + fibonacci(n - 2)

nums = int(input("Fibonacci numbers to show: "))

if nums <= 0: print("Must be a positive integer")
else:
    print("Fibonacci series: ")
    for i in range(nums): print(fibonacci(i), end = ' ')

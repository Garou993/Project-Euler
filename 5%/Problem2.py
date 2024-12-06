# Even Fibonacci Numbers

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fib(n-1)+fib(n-2)


ans = 0
for i in range(2,33):
    if fib(i) % 2 == 0:
        ans += fib(i) 
print(ans)
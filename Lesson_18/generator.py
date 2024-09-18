# 1 A generator that rotates the sequence of paired numbers from 0 to N:

def even_numbers(N):
    for i in range(0, N + 1, 2):
        yield i


N = 10
for num in even_numbers(N):
    print(num)


# 2 A generator that generates the Fibonacci sequence up to the number N:

def fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


N = 50
for num in fibonacci(N):
    print(num)

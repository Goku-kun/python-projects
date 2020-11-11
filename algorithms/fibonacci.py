def fibonacci(n, a=0, b=1):
    L = []
    while len(L) < n:
        L.append(a)
        a, b = b, a+b
    return L

print(fibonacci(5))
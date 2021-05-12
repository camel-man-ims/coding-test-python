def multiple(n):
    if n == 1:
        return 1
    return n * multiple(n-1)

def add(n):
    if n == 1:
        return 1
    return n + add(n-1)


print(multiple(10))
print(add(10))
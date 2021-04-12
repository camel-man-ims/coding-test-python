n = int(input())

mem = []

for i in range(45):
    mem.append(0)


def fibonacci(m):
    if m == 1:
        return 1
    if m == 2:
        return 1

    if mem[m]==0:
        mem[m] = fibonacci(m-1) + fibonacci(m-2)
    return mem[m]

i = fibonacci(n)

print(i)

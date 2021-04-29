num = int(input())
answer = 0

for i in range(1, num + 1):
    value = list(map(int, str(i)))
    answer = i + sum(value)

    if answer == num:
        print(i)
        break

    if i == num:
        print(0)
N = int(input())

cnt = 0
answer = ""

def hanoi(n, start, end):
    global cnt
    global answer
    cnt += 1
    if n == 1:
        temp = str(start) + " " + str(end) + "\n"
        answer += temp
        return

    hanoi(n - 1, start, 6 - start - end)
    temp = str(start) + " " + str(end) + "\n"
    answer += temp
    hanoi(n - 1, 6 - start - end, end)


hanoi(N,1,3)
print(cnt)
print(answer)
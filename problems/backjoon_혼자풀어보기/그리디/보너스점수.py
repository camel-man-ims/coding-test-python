# 21.05.30

n = int(input())
s = input()

score = 0
bonus = 0

for i in range(len(s)):
    if s[i] == 'O':
        score += i+1
        score+=bonus
        bonus +=1
    else:
        bonus=0

print(score)
# 21.05.03

n = int(input())

person = []
for _ in range(n):
    weight, height = map(int,input().split())
    person.append((weight,height))

bigger = []

for i in range(n):
    count = 0
    for j in range(n):
        if i==j:
            continue
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            count +=1
    bigger.append(count)

queue_arr = []

for i in range(n):
    queue_arr.append([i,bigger[i]])

queue_arr.sort(key=lambda x:x[1])

grade = 1
temp = 1
grade_arr = []

while queue_arr:
    pop = queue_arr.pop(0)
    if not queue_arr:
        pop[1] = grade
    elif pop[1] != queue_arr[0][1]:
        pop[1]=grade
        grade += temp
        temp=1
    else:
        pop[1] = grade
        temp +=1
    grade_arr.append(pop)

grade_arr.sort(key=lambda x:x[0])

for num in grade_arr:
    print(num[1],end=' ')

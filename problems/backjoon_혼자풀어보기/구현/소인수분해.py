# 21.06.08
# 11653번
# 나누어 떨어지는 것을 어떻게 판단? = 나머지가 0이면 나누어 떨어짐

target = int(input())

divide = 2

while target!=1:
    if target%divide==0:
        target = target/divide
        print(divide)
    else:
        divide+=1

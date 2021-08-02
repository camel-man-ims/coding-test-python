n= int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다. ")
s = "\"재귀함수가 뭔가요?\"\n\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
print(s)

index = 1

def recurse(s_value):
    global index

    # 라인 붙이기
    line =""
    for i in range(4*index):
        line += "_"
    index+=1
    split_arr = s_value.split("\n")
    for i in range(len(split_arr)):
        split_arr[i] = line + split_arr[i]
    result_string = ""

    # 문자열 잇기
    for s_indi in split_arr:
        result_string += s_indi + "\n"
    result_string = result_string[0:len(result_string)-1]
    print(result_string)

def recurse_last():
    global index
    line =""
    for i in range(4*index):
        line += "_"
    s_1 = "\"재귀함수가 뭔가요?\""
    s_1 = line+s_1

    s_2 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
    s_2 = line+s_2

    print(s_1)
    print(s_2)

def recurse_reverse():
    global index
    index-=1

    line =""
    for i in range(4*index):
        line += "_"
    s_1 = "라고 답변하였지."
    s_1 = line + s_1
    print(s_1)

while index<n:
    recurse(s)

recurse_last()

index+=1

while index>0:
    recurse_reverse()

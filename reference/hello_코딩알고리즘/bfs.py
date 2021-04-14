# 21.04.14
# set 으로 선언하면, queue 에 append 하지 않고 바로 집어넣을 수 있다
# 이 때, key 의 값들만 들어가게 된다
# 그래서 값을 꺼내고 dict() 형으로 key - value 를 꺼내서 확인할 수 있다


from collections import deque

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

queue = deque()
queue += graph["you"]

searched=[]

def person_is_seller(name):
    return name[-1]=='m'

while queue:
    person = queue.popleft()
    print(queue)
    if person not in searched:
        if person_is_seller(person):
            print(person + " is seller")
        else:
            queue += graph[person]
            searched.append(person)

print(searched)
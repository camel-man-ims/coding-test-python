from collections import deque

def solution(bridge_length, weight, truck_weights):

    q_truck = deque()
    q_bridge = deque()
    q_temp = deque()

    count = 0

    for i in truck_weights:
        q_truck.append(i)

    while q_truck or q_bridge:
        # 추가
        count +=1
        if len(q_bridge) <= bridge_length and weight >=0 and q_truck:
            pop_bus = q_truck.popleft()
            if weight -pop_bus >=0:
                q_bridge.append([pop_bus,0])
                weight -= pop_bus
        # 조회
        while q_bridge:
            q_temp.append(q_bridge.popleft())
        while q_temp:
            pop_bus = q_temp.popleft()
            q_bridge.append([pop_bus[0],pop_bus[1]+1])
        i = 0
        q_length = len(q_bridge)
        while i<q_length:
            pop_bus = q_bridge.popleft()
            if pop_bus[1] <= bridge_length:
                q_bridge.append(pop_bus)
            i+=1
        if len(q_bridge) <= bridge_length and weight >=0 and q_truck:
            pop_bus = q_truck.popleft()
            if weight -pop_bus >=0:
                q_bridge.append([pop_bus,0])
                weight -= pop_bus
    print(count)
    answer = 0
    return answer


solution(2,10,[7,4,5,6])
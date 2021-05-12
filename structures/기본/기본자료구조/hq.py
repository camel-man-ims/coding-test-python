import heapq

def heap(arr):
    h = []
    result = []

    for val in arr:
        heapq.heappush(h,-val)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(heap([123,43,21,1,2,3,5,10]))

# heapq 위에서 동작한다.

# 힙 =[]
# heapq.heappop(힙)
# heapq.heappush(힙,data)
import heapq

def heap(arr):
    h = []
    result = []

    for data in arr:
        heapq.heappush(h,-data)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(heap([43,11,1121,32]))
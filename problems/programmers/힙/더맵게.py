# 21.05.06
import heapq

def solution(scoville, K):
    heap_arr = []
    count =0
    for num in scoville:
        heapq.heappush(heap_arr,num)
    while heap_arr[0] <K:
        if len(heap_arr) <2:
            count = -1
            break
        pop_first = heapq.heappop(heap_arr)
        pop_second = heapq.heappop(heap_arr)
        new_num = pop_first + pop_second*2
        heapq.heappush(heap_arr,new_num)
        count +=1
    return count


re = solution([1, 2, 3, 9, 10, 12], 7)
print(re)

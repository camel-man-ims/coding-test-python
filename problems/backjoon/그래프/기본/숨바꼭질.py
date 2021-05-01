# 21.04.20
from collections import deque

MAX = 100001
n,k = map(int,input().split())
array = [0]* MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos==k:
            return array[now_pos]
        # in 에 여러 숫자가 들어갈 수 있다
        for next_pos in (now_pos-1,now_pos+1,now_pos*2):
            # 값이 0이면 false, 0이상이면 True 인데, [0]은 True 다
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] +1
                q.append(next_pos)

print(bfs())
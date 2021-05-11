# 파이썬에서 헤더를 클래스 내에서 선언해서 다루는 방법을 모르겠다...
# 맨 앞의 노드를 삭제해야 하는 경우가 생길 때는, 그냥 노드 하나를 더 추가해놓고 그것을 header 로 사용하면 될 것 같다
# 21.05.11
import time
from itertools import combinations

start = time.time()

class Node:
    def __init__(self,data,next=None):
        self.val = data
        self.next = next
    def retrieve(self):
        node = self
        while node.next:
            if node.val !=None:
                print(node.val)
            node=node.next
        print(node.val)
    def append(self,data):
        node = self
        while node.next:
            node=node.next
        node.next = Node(data)
    # 특정 값 뒤에 추가하기
    def append_number(self,data,insert_number):
        node = self
        while True:
            if node.val == insert_number:
                break
            else:
                node=node.next
        next_address = node.next
        node.next = data
        data.next = next_address
    def delete(self,data):
        node = self
        while node.next:
            if node.next.val == data:
                node.next = node.next.next
            else:
                node=node.next


node1 = Node(None)
node1.append(1)
node1.append(2)
node1.append(3)
node1.append(4)

node1.delete(1)

node1.retrieve()

arr = [1,2,3,4,5,6,7,8,101010,101]


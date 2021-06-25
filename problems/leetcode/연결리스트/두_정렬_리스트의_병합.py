# 왜 안되는지 모르겠다 보류...
# 두 노드를 비교해서, 작은 노드를 새로운 노드에 이어붙여주고, 한 쪽이 None 이면 나머지 모두를 이어붙이게 풀었는데
# current 가 다음 값이 안되네

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def add(self,val):
        node = self

        while node.next is not None:
            node=node.next
        new_node=Node(val)
        node.next=new_node
    def print(self):
        node = self
        while node is not None:
            print(node.val)
            node=node.next

def merge(node1,node2):
    current = None
    if node1.val > node2.val:
        current = Node(node2.val)
        node2=node2.next
    else:
        current = Node(node1.val)
        node1=node1.next

    while node1 is not None and node2 is not None:
        if node1.val > node2.val:
            current.next = Node(node2.val)
            current = current.next
            node2 = node2.next
        else:
            current.next = Node(node1.val)
            current = current.next
            node1 = node1.next
        print(" ==== ")
        current.print()


        if node1 is None:
            current.next = node2
        if node2 is None:
            current.next = node1
    return current

n1 = Node(1)
n1.add(2)
n1.add(4)

n2 = Node(1)
n2.add(3)
n2.add(4)

node = merge(n1,n2)
node.print()
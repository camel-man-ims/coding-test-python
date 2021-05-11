# 21.05.10

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def append(d):
    node = head
    while node.next:
        node = node.next
    new_node = Node(d)
    node.next=new_node

def search():
    node = head
    while node.next:
        print(node.data)
        node=node.next
    print(node.data)

node1 = Node(1)
node2 = Node(2)

node1.next = node2

head = node1

for i in range(3,10):
    append(i)

search()
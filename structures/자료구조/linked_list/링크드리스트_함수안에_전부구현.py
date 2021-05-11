# 21.05.10

class Node:
    def __init__(self,data,next=None):
        self.val = data
        self.next = next
    def retrieve(self):
        node = self
        while node.next:
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
    def delete(self,data,head):
        node = self
        while node.next:
            if node.next.val == data:
                node.next = node.next.next
            else:
                node=node.next


node1 = Node(1)
node1.append(2)
node1.append(3)
node1.append(4)

node2 = Node(5)

node1.append_number(node2,2)


node1.retrieve()
node1.retrieve()
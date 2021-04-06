class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def add(self, data):
        node = self
        while node.next is not None:
            node = node.next
        newNode = Node(data)
        node.next=newNode

    def search(self):
        node = self
        while node.next is not None:
            print(node.data)
            node=node.next

        print(node.data)

n = Node(1)
n.add(2)
n.add(3)

n.search()



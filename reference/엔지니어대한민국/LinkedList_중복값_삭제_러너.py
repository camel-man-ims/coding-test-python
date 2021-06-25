# https://www.youtube.com/watch?v=Ce4baygLMz0

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def add(self,val):
        node = self
        while node.next is not None:
            node=node.next
        node.next = Node(val)
    def print(self):
        node = self
        while node:
            print(node.val)
            node=node.next

    def remove_duplicate(self):
        node = self
        while node is not None and node.next is not None:
            runner = node
            while runner.next is not None :
                if node.val == runner.next.val:
                    runner.next =runner.next.next
                else:
                    runner=runner.next
            node=node.next

n1 = Node(1)
n1.add(2)
n1.add(3)
n1.add(3)
n1.add(4)
n1.add(4)
n1.add(4)
n1.add(4)
n1.add(5)

n1.remove_duplicate()
n1.print()

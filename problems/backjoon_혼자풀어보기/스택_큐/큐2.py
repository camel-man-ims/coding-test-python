# 21.06.18

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueImpl:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self,val):
        node = Node(val)
        if self.last is not None:
            self.last.next = node
        self.last=node
        if self.first is None:
            self.first=self.last
    def pop(self):
        if self.first is None:
            return -1
        first = self.first.val
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return first
    def size(self):
        count =0
        node = self.first
        while node is not None:
            count +=1
            node=node.next
        return count
    def empty(self):
        if self.first is None:
            return 1
        else:
            return 0
    def front(self):
        if self.first is None:
            return -1
        return self.first.val
    def back(self):
        node = self.first
        while node.next is not None:
            node=node.next
        return node.val
    def print(self):
        node = self.first

        while node is not None:
            print(node.val)
            node=node.next

n = int(input())

q = QueueImpl()

for _ in range(n):
    temp = []
    temp_arr = input().split()
    for i in temp_arr:
        temp.append(i)

    if temp[0] == 'push':
        q.push(temp[1])
    elif temp[0] == 'pop':
        print(q.pop())
    elif temp[0] == 'size':
        print(q.size())
    elif temp[0] == 'empty':
        print(q.empty())
    elif temp[0] == 'front':
        print(q.front())
    elif temp[0] == 'back':
        print(q.back())
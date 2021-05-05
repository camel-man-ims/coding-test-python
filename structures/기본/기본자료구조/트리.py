class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

arr = dict()
arr[1] = Node(1,2,5)
arr[2] = Node(2,2,5)

print(arr[1].data)

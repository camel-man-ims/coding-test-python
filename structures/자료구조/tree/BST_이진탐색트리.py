# 21.05.11
# 이진트리 = 자식이 최대 2개인 트리
# 이진 탐색 트리 = Binary Search Tree
# 이진트리 + 규칙
# 왼쪽은 무조건 오른쪽보다 작고, 오른쪽은 무조건 왼쪽보다 크다
# Tree = 노드와 브랜치(선)로 이루어진 사이클이 없는 데이터 구조

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, val):
        self.root = Node(val)

    def append(self, val):
        # root 의 참조변수 값을 변하지 않게 하기 위해 새로운 노드를 생성해서 넣어줌
        self.current_node = self.root
        while True:
            if val > self.current_node.val:
                if self.current_node.right is None:
                    self.current_node.right = Node(val)
                    break
                else:
                    self.current_node = self.current_node.right
            else:
                if self.current_node.left is None:
                    self.current_node.left = Node(val)
                    break
                else:
                    self.current_node = self.current_node.left

    def search_number(self, val):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.val == val:
                return True
            elif val < self.current_node.val:
                self.current_node = self.current_node.left
            elif val > self.current_node.val:
                self.current_node = self.current_node.right
        return False

    def print_right_numbers(self):
        self.current_node = self.root
        while self.current_node:
            print(self.current_node.val)
            self.current_node=self.current_node.right

    def print_left_numbers(self):
        self.current_node = self.root
        while self.current_node:
            print(self.current_node.val)
            self.current_node=self.current_node.left


node = BST(3)
node.append(4)
node.append(5)
node.append(6)

print(node.search_number(4))
node.print_right_numbers()
node.print_left_numbers()
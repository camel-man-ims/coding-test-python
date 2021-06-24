# https://leetcode.com/problems/palindrome-linked-list/
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()
        node = head
        while node:
            q.append(node.val)
            node=node.next
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True
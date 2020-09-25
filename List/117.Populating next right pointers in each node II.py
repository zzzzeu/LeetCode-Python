"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        pre = root
        dummy = Node(0)

        while pre:
            temp = dummy
            while pre:
                if pre.left:
                    temp.next = pre.left
                    temp = temp.next
                if pre.right:
                    temp.next = pre.right
                    temp = temp.next
                pre = pre.next
            pre = dummy.next
            if temp == dummy:
                break
        
        return root
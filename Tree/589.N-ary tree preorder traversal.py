"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res =[]
        def helper(root):
            if not root:
                return 
            res.append(root.val)
            for cur in root.children:
                helper(cur)
        helper(root)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack,res = [root], []
        while stack:
            cur = stack.pop(-1)
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        return res


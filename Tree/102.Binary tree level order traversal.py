# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        layer = collections.deque()
        layer.append(root)
        res = []
        while layer:
            temp = [] 
            for _ in range(len(layer)): 
                node = layer.popleft() 
                temp.append(node.val)
                if node.left: 
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(temp) 
        return res

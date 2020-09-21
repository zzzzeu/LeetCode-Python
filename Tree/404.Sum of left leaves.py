# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(node):
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                self.res += node.left.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}

        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
            head = head.next
        
        return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return False
            if slow == fast:
                return True

        return False
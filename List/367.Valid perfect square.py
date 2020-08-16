class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True       
        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            x = mid * mid
            if x == num:
                return True
            if x > num:
                right = mid - 1
            else:
                left = mid + 1      
        return False

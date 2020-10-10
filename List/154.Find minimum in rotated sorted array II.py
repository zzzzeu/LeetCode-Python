class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        n = len(nums)
        for i in range(0,n - 1):
           if nums[i + 1] < nums[i]:
                return nums[i + 1]
        return nums[0]
 
        
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else: 
                right -= 1
        return nums[left]

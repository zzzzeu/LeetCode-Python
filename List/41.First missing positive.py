class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                self._swap(nums, i, nums[i] - 1)
            
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        
        return n + 1

    def _swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                lenth = 1

                while current + 1 in nums_set:
                    current += 1
                    lenth += 1
                
                res = max(res, lenth)
        
        return res
        
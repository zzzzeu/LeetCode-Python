class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = nums[0]
        res = temp
        n = len(nums)
        for i in range(1, n):
            if temp + nums[i] > nums[i]:
                temp += nums[i]
                res = max(res, temp)
            else:
                res = max(res, nums[i])
                temp = nums[i]
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > n // 2:
                return num
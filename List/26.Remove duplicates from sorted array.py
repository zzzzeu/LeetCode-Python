class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                if j - i > 1:
                    nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1
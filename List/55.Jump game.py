class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:
                right = max(right, i + nums[i])
                if right >= n - 1:
                    return True
        return False

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left,right = 0, n - 1 
        maxleft,maxright = height[0],height[n - 1]
        res = 0
        while left <= right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                res += maxleft - height[left]
                left += 1
            else:
                res += maxright - height[right]
                right -= 1
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        res = 0
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        for i in range(1,n):
            maxleft[i] = max(height[i],maxleft[i-1])
        for j in range(n-2,-1,-1):
            maxright[j] = max(height[j],maxright[j+1])
        for i in range(n):
            if min(maxleft[i],maxright[i]) > height[i]:
                res += min(maxleft[i],maxright[i]) - height[i]
        return res
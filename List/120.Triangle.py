class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for row in range(n-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col],triangle[row+1][col+1])
        return triangle[0][0]

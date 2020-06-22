class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        row = 0
        col = cols
        while row <= rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
        
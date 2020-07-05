class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': 
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            grid[i][j] = '0'
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in dirs:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
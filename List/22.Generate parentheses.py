class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = ''

        def dfs(temp: str, left: int, right: int):
            if left == 0 and right == 0:
                res.append(temp)
                return
            if right < left:
                return
            if left > 0:
                dfs(temp + '(', left - 1, right)
            if right > 0:
                dfs(temp + ')', left, right - 1)
    
        dfs(temp, n, n)
        return res
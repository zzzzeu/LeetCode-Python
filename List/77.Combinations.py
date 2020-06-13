class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]       
        res = self.combine(n - 1, k)
        for i in self.combine(n - 1, k - 1):
            i.append(n)
            res.append(i)        
        return res
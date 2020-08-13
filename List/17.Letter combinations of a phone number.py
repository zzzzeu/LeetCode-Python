class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dic = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        res = []

        def backtrack(temp, string):
            if len(string) == 0:
                res.append(temp)
            else:
                for char in dic[string[0]]:
                    backtrack(temp + char, string[1:])

        backtrack('', digits)
        return res
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # stack = [i for i in S if i.isalpha()]
        # res = []
        # for i in S:
        #     if i.isalpha():
        #         res.append(stack.pop())
        #     else:
        #         res.append(i)
        # return "".join(res)

        res = []
        j = len(S) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(x)
        
        return "".join(res)
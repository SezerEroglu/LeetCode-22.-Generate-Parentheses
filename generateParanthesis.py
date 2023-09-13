from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        allStack = []
        res = []

        def backtrack(openParan, closeParan):
            if openParan == closeParan == n:
                res.append("".join(allStack))
            if openParan < n:
                allStack.append("(")
                backtrack(openParan + 1, closeParan)
                allStack.pop()
            if closeParan < openParan:
                allStack.append(")")
                backtrack(openParan, closeParan + 1)
                allStack.pop()

        backtrack(0, 0)
        return res


sol = Solution()
sol.generateParenthesis(2)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(p, left, right):
            if left == 0 and right == 0: 
                yield p
            if left > 0:
                yield from backtrack(p + '(', left - 1, right)
            if right > left:
                yield from backtrack(p + ')', left, right - 1)

        return list(backtrack('', n, n))
        

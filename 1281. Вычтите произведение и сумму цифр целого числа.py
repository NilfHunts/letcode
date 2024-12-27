class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval('*'.join(str(n))) - sum(map(int, str(n)))

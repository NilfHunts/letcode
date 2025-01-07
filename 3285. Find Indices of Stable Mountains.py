class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i, [num1,num2] in enumerate(pairwise(height),start=1):
            if num1 > threshold:
                ans.append(i)
        return ans

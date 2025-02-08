class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits))) + 1
        arr = [int(digit) for digit in str(result)]
        return arr

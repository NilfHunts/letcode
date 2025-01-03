class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        all_sum = sum(nums)  
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):  
            left_sum += nums[i]  
            right_sum = all_sum - left_sum  
            if left_sum >= right_sum:  
                count += 1
        return count

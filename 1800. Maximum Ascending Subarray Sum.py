class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        ans = 0
        sdf = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                sdf += nums[i]
            else:  
                ans = max(ans, sdf)
                sdf = nums[i]  
         
        return max(ans, sdf)
        

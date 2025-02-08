class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1 
        ans = []
        sdf = 1
        sdfg = 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sdf += 1
            else:  
                ans.append(sdf)
                sdf = 1
            if nums[i] < nums[i + 1]:
                sdfg += 1
            else:  
                ans.append(sdfg)
                sdfg = 1
                print(sdfg,sdf)     
        ans.append(sdf)
        ans.append(sdfg)  
        return max(ans)


            

            

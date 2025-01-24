for i in range(k):
            ans_1 = min(nums)
            index = nums.index(ans_1)
            llkj = ans_1 * multiplier
            nums[index] = llkj
        return nums

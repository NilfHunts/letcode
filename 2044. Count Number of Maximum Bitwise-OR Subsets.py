class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = defaultdict(int)  # Хранит количество подмножеств для каждого значения OR
        dp[0] = 1  # Начальное значение: одно пустое подмножество

        max_or = 0
        for num in nums:
            new_dp = dp.copy()
            for current_or in dp:
                new_or = current_or | num
                new_dp[new_or] += dp[current_or]
                max_or = max(max_or, new_or)
            dp = new_dp

        return dp[max_or]

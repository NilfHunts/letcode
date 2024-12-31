class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)  #+первый день поездки
        days_set = set(days)  #множество для поиска

        for i in range(1, len(dp)):
            if i not in days_set:
                dp[i] = dp[i - 1]  #если нет дня стоимость не меняется
            else:
                #какой вариант будет минимальным
                dp[i] = min(dp[i - 1] + costs[0],  #1-вар. билета
                            dp[max(0, i - 7)] + costs[1],  #2-вар. билета
                            dp[max(0, i - 30)] + costs[2])  #3-вар билета
        
        return dp[-1]  #вернуть минимальную цену

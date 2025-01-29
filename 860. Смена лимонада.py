class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FIVE = 0
        TEN = 0     
        for i in bills:
            if i == 5:
                FIVE += 5
            elif i == 10 and FIVE >= 5:
                FIVE -= 5
                TEN += 10
            elif i == 10 and FIVE == 0:
                return False
            elif i == 20:
                if FIVE >=5 and TEN >= 10:
                    FIVE -= 5
                    TEN -= 10
                elif FIVE >= 15:
                    FIVE -= 15
                else:
                    return False
        return True
        
        
        

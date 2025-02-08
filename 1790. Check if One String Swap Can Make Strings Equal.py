class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a = 0
        for x, y in zip(s1, s2):
            if x != y:
                a+=1
                
                if a==1:
                    swappa = (x,y)
                elif a==2:
                    if swappa!=(y,x):return False
                else: return False

        return a!=1

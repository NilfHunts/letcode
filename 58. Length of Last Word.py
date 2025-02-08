class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        c = s.split()
        return len(c[-1])
        
        

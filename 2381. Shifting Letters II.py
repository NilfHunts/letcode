class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    
        n = len(s)
        shift_array = [0] * (n + 1)
        
        # Populate the shift array with the net shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end + 1] += 1
        
        # Calculate the prefix sum to determine the cumulative shift at each index
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        # Apply the shifts to the string
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + shift_array[i]) % 26
            result.append(chr(ord('a') + shift))
        
        return ''.join(result)

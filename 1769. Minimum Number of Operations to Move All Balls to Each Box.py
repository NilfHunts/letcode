class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # First pass: from left to right
        count = 0  # Tracks the number of balls encountered so far
        operations = 0  # Tracks the number of operations so far
        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count  # Add the current count of balls to operations
        
        # Second pass: from right to left
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count  # Add the current count of balls to operations

        return answer
      
        
        

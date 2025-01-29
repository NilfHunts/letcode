class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid [r][c] == 0:
                    continue
                q = deque([(r,c)]) 
                ripka = grid [r][c]
                grid [r][c] = 0
                while q:
                    row,col = q.popleft()
                    if row !=0 and grid[row-1][col]:
                        ripka += grid [row-1][col]
                        grid [row-1][col] = 0
                        q.append([row-1,col])
                    if row!=len(grid)-1 and grid[row+1][col]:
                        ripka += grid [row+1][col]
                        grid [row+1][col] = 0
                        q.append([row+1,col])
                    if col !=0 and grid[row][col-1]:
                        ripka += grid [row][col-1]
                        grid [row][col-1] = 0
                        q.append([row,col-1])
                    if col !=len(grid [0])-1 and grid[row][col+1]:
                        ripka += grid [row][col+1]
                        grid [row][col+1] = 0
                        q.append([row,col+1])
                if ans<ripka:
                    ans = ripka
        return ans



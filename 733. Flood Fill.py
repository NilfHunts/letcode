class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ochered = deque([[sr,sc]])
        see = set((sr,sc))
        col = image[sr][sc]
        if color == col: return image
        while ochered:
            r, c = ochered.popleft()
            image[r][c] = color
            if c !=0 and image[r][c-1] == col and (r,c-1) not in see:
                see.add((r,c-1))
                ochered.append((r,c-1))
            if c !=len(image[0])-1 and image[r][c+1] == col and (r,c+1) not in see:
                see.add((r,c+1))
                ochered.append((r,c+1))
            if r !=0 and image[r-1][c] == col and (r-1,c) not in see:
                see.add((r-1,c))
                ochered.append((r-1,c))
            if r !=len(image)-1 and image[r+1][c] == col and (r+1,c) not in see:
                see.add((r+1,c))
                ochered.append((r+1,c))
        return image


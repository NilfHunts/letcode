class Solution:
    def maxArea(self, height: List[int]) -> int:
        #правые и левые числа
        left = 0  
        right = len(height) - 1
        #максимальная площадь  
        max_area = 0  
        #указатели пока не встретятся
        while left < right: 
            #находим полщадь
            area = (right - left) * min(height[left], height[right])
            #изменение площади
            max_area = max(max_area, area) 
            
            #изменяем указатели
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        #возвращаем обьем
        return max_area

class Solution:
        def countAlternatingGroups(colors):
            n = len(colors)
            count = 0

        for i in range(n):
        # Индексы трех плиток с учетом кругового массива
            a, b, c = colors[i], colors[(i + 1) % n], colors[(i + 2) % n]
        
        # Проверяем, что средняя плитка отличается от соседних
        if a != b and b != c and a != c:
            count += 1

        return count

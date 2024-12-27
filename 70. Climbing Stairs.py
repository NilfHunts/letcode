class Solution:
    def climbStairs(self, n: int) -> int:
        fibo = [1, 2, 3]  # Начальные значения последовательности

        def find(num):
            # Используем локальную переменную fibo
            if num <= len(fibo):
                return fibo[num - 1]  # Возвращаем из списка
            # Если требуемый элемент ещё не рассчитан, вычисляем его
            fibo.append(find(num - 1) + find(num - 2))
            return fibo[-1]  # Возвращаем последний добавленный элемент

        return find(n)

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []  # Используем список для временного хранения сумм
        temp_sum = 0  # Сумма значений между нулями
        
        # Итерация по связанному списку
        while head:
            if head.val == 0:  # Если встречаем 0
                if temp_sum > 0:  # Если сумма ненулевая, добавляем её в список
                    ans.append(temp_sum)
                    temp_sum = 0  # Сбрасываем сумму
            else:
                temp_sum += head.val  # Суммируем значения узлов между нулями
            head = head.next  # Переходим к следующему узлу
        
        # Создаем новый связанный список из накопленных сумм
        dummy = ListNode(0)  # Вспомогательный узел
        current = dummy
        for value in ans:
            current.next = ListNode(value)
            current = current.next
        
        return dummy.next  # Возвращаем голову нового списка

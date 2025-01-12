class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        # Баланс и возможные изменения
        balance = 0
        flex = 0

        # Один проход слева направо и одновременно справа налево
        for i in range(len(s)):
            # Слева направо
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1

            # Справа налево
            rev_i = len(s) - 1 - i
            if locked[rev_i] == '0' or s[rev_i] == ')':
                flex += 1
            else:
                flex -= 1

            # Проверка на невозможность баланса
            if balance < 0 or flex < 0:
                return False

        return True

    
        

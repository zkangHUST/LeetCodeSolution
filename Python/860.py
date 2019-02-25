class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0, 10:0, 20:0}
        for val in bills:
            if val == 5:
                money[5] += 1
            elif val == 10:
                if money[5] >= 1:
                    money[5] -= 1
                    money[10] += 1
                else:
                    return False
            elif val == 20:
                if money[10] >= 1 and money[5] >= 1:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
                money[20] += 1
        return True
        

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0  # Number of $5 and $10 bills we have
        
        for bill in bills:
            if bill == 5:
                five += 1
            
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False  # No $5 to give change
            
            else:  # bill == 20
                if ten > 0 and five > 0:  # Prefer giving 10 + 5
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise, give 3 fives
                    five -= 3
                else:
                    return False  # Can't give change
        
        return True

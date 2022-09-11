from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    if len(digits) == 1 and digits[0] == 9:   # when digits = 9
        return [1,0]
    if digits[-1] != 9:   # when last digit is not 9
        digits[-1] = digits[-1] + 1
        return digits
    else:
        digits[-1] = 0   # when last digit is 9, then change the last digit to 0 
                         # and recurse digits[:-1]
        digits[:-1] = self.plusOne(digits[:-1])
        return digits
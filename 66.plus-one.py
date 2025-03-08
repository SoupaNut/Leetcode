#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        
        # take care of 9's
        while abs(i) <= len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1
            
        # if all 9's
        if abs(i) > len(digits):
            digits.insert(0,1)
        else:
            digits[i] += 1
            
        return digits
# @lc code=end


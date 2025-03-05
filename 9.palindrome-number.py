#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_str = str(x)
        total_digits = len(int_str)
        left = 0
        right = total_digits - 1
        
        while left < right:
            if int_str[left] != int_str[right]:
                return False
            left += 1
            right -= 1
            
        return True
            
        
# @lc code=end


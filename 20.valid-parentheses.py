#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # keeps track of open parentheses
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        # only return true if our stack is empty
        return not stack
        
        
        
        
# @lc code=end


#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        for c in reversed(s):
            # skip over spaces at the end if we haven't found a character yet
            if c == " " and length == 0:
                continue
            
            # if we find a space after finding a character, we've reached the end of the last word
            if c== " ":
                break
            
            length += 1
            
        return length
    
                 
# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        longest_length = 0
        
        for i in range(len(s)):
            current_str = s[i]
            
            for j in range(i + 1, len(s)):
                if s[j] not in current_str:
                    current_str += s[j]
                elif len(current_str) > longest_length:
                    longest_length = len(current_str)
                    break;
                else:
                    break;
            
            if len(current_str) > longest_length:
                longest_length = len(current_str)
        
        return longest_length
# @lc code=end


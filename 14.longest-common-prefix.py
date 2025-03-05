#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        
        # we can choose any string to compare with the rest
        for c in range(len(strs[0])):
            current_char = strs[0][c]
            try:
                if all([s[c] == current_char for s in strs]):
                    common_prefix += current_char
                else:
                    break;
            # if we get an IndexError, it means that we have reached the end of the shortest string
            except IndexError:
                break;
            
        return common_prefix
            
# @lc code=end


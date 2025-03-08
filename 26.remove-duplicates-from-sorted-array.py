#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_nums = set()
        length = len(nums)
        
        for i, num in reversed(list(enumerate(nums))):
            if num in seen_nums:
                nums.pop(i)
                length -= 1
            else:
                seen_nums.add(num)
                
        return length
# @lc code=end


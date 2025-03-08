#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        
        while val in nums:
            nums.remove(val)
            length -= 1
            
        return length
            
# @lc code=end


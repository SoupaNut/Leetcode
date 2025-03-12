#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        total_elements = len(nums)

        pos = 0
        neg = 0

        for i in range(total_elements):
            if nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                pos = total_elements - i
                break

        return max(pos, neg)
        
# @lc code=end


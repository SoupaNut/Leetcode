#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k is the number to update next time

        total_nums = len(nums)

        if total_nums <= 2:
            return total_nums

        k = 2

        # i is the current index number
        # we start at 2 since each unique element appears at most twice
        for i in range(2, total_nums):
            # move the k pointer if we find a differing number
            # we check k-2 since we need to check if it's a duplicate that's appearing more than twice or not
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k
        
# @lc code=end


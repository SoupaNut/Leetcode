#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        nums.sort()
        print(nums)
        
        for i in range(len(nums)):
            smallest = nums[i]
            
# @lc code=end


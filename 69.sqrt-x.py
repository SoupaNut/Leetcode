#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid -1 
        return right
# @lc code=end


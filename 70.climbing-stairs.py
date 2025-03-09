#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        ways = [0] * (n+1)
        ways[1] = 1
        ways[2] = 2
        ways[3] = 3
        
        for i in range(4, n+1):
            ways[i] = ways[i-1] + ways[i-2]
            
        return ways[n]
        
# @lc code=end


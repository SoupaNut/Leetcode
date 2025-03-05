#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ----- SOLUTION 3: The last position where each character was seen
        left = max_length = 0
        last_seen = {}
        
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
                
            max_length = max(max_length, right - left + 1)
            last_seen[c] = right
            
        return max_length
        
        
        # ----- SOLUTION 2: Sliding Window & Hashmap
        # left = max_length = 0
        # count = {}
        # for right, c in enumerate(s):
        #     count[c] = count.get(c, 0) + 1
        #     while count[c] > 1:
        #         count[s[left]] -= 1
        #         left += 1
            
        #     max_length = max(max_length, right - left + 1)
        
        # return max_length
        
        
        
        # ----- SOLUTION 1: Sliding Window & Set
        # left = 0 # pointer of the sliding window
        # max_length = 0 # this is the value we should return
        # char_set = set() # this is to keep the current chars forming the longest substring w/ the two conditions above
        # # NOTE: a set is unordered, unchangeable (only the items are unchangeable but you can add or remove items), and unindexed
        
        
        # # iterate through all chars one by one and create right pointer of sliding window w/ for loop
        # for right in range(len(s)):
            
        #     # we use a while loop to remove multiple characters since we need the substring
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1

        #     # add the right char to the set once we are done with the loop
        #     char_set.add(s[right])
            
        #     # only update the max length if the current substring is longer
        #     max_length = max(max_length, right - left + 1)

        # return max_length
    
    
        # ----- BELOW IS MY FIRST ATTEMPT:
        # if len(s) == 1:
        #     return 1
        
        # longest_length = 0
        
        # for i in range(len(s)):
        #     current_str = s[i]
            
        #     for j in range(i + 1, len(s)):
        #         if s[j] not in current_str:
        #             current_str += s[j]
        #         elif len(current_str) > longest_length:
        #             longest_length = len(current_str)
        #             break;
        #         else:
        #             break;
            
        #     if len(current_str) > longest_length:
        #         longest_length = len(current_str)
        
        # return longest_length
# @lc code=end


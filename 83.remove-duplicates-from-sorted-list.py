#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head # save the beginning of the linked list to return later
        
        while head and head.next:
            # check if the current and next val are the same
            if head.val == head.next.val:
                # if they are, skip the next node
                head.next = head.next.next
            else:
                head = head.next
                
        return result
                
# @lc code=end


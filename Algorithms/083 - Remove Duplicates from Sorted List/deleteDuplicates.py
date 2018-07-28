# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        anchor = None
        while curr:
          if anchor is None:
            anchor = curr
          else:
            if curr.val == anchor.val:
              anchor.next = curr.next
            else:
              anchor = curr
          curr = curr.next
        return head

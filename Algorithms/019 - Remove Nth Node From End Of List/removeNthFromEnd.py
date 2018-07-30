# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        if n == len(nodes):
            if len(nodes) != 1:
                return nodes[1]
        else:
            nodes[-(n + 1)].next = nodes[-n].next
            return nodes[0]

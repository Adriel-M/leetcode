class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        ret = head
        prev = None
        curr = head
        curr_next = head.next
        i = 0
        while curr_next:
            tmp = curr_next.next
            if i % 2 == 0:
                if ret == head:
                    ret = curr_next
                curr_next.next = curr
                curr.next = None
                if prev:
                    prev.next = curr_next
                prev = curr_next
            else:
                prev = curr
                curr = curr_next
            curr_next = tmp
            prev.next = curr
            curr.next = curr_next
            i += 1
        return ret

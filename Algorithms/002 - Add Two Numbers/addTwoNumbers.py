class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev_value = 0
        l1_curr = l1
        l2_curr = l2
        ret = None
        curr = None
        while l1_curr is not None or l2_curr is not None:
            l1_num = 0
            l2_num = 0
            if l1_curr is not None:
                l1_num = l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr is not None:
                l2_num = l2_curr.val
                l2_curr = l2_curr.next
            res = l1_num + l2_num + (prev_value // 10)
            prev_value = res
            if ret is None:
                ret = ListNode(res % 10)
                curr = ret
            else:
                curr.next = ListNode(res % 10)
                curr = curr.next
        if prev_value >= 10:
            curr.next = ListNode(prev_value // 10)
        return ret

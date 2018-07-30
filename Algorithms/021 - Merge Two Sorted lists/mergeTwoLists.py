class Solution:
    def mergeTwoLists(self, l1, l2):
        l1_curr = l1
        l2_curr = l2
        ret = []
        while l1_curr is not None or l2_curr is not None:
            if l1_curr is None:
                ret.append(l2_curr)
                l2_curr = l2_curr.next
            elif l2_curr is None:
                ret.append(l1_curr)
                l1_curr = l1_curr.next
            else:
                if l1_curr.val > l2_curr.val:
                    ret.append(l2_curr)
                    l2_curr = l2_curr.next
                else:
                    ret.append(l1_curr)
                    l1_curr = l1_curr.next
        for i in range(len(ret)):
            if i == len(ret) - 1:
                ret[i].next = None
            else:
                ret[i].next = ret[i + 1]
        if len(ret) > 0:
            return ret[0]
        else:
            return None

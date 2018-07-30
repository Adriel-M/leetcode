from queue import PriorityQueue


class PItem:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority


class Solution:
    def mergeKLists(self, lists):
        ret = None
        curr = None
        min_queue = PriorityQueue()
        for llist in lists:
            if llist:
                min_queue.put(PItem(llist.val, llist))
        while not min_queue.empty():
            best = min_queue.get().item
            if ret is None:
                ret = best
            if curr is None:
                curr = best
            else:
                curr.next = best
                curr = curr.next
            if best.next:
                min_queue.put(PItem(best.next.val, best.next))
        return ret

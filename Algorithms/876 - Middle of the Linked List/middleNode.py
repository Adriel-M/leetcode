class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        mid = int(len(nodes) / 2)
        return nodes[mid]

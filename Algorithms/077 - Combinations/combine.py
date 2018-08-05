class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        curr = []

        def generate(curr_pos):
            if len(curr) == k:
                ret.append(curr[:])
            else:
                for i in range(curr_pos, n):
                    curr.append(i + 1)
                    generate(i + 1)
                    curr.pop()
        generate(0)
        return ret

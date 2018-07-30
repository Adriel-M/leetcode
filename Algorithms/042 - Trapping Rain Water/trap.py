class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        ret = 0
        i_max = 0
        j_max = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] > i_max:
                    i_max = height[i]
                elif height[i] < i_max:
                    ret += i_max - height[i]
                i += 1
            else:
                if height[j] > j_max:
                    j_max = height[j]
                elif height[j] < j_max:
                    ret += j_max - height[j]
                j -= 1
        return ret

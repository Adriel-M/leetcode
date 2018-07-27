class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        best_i = 0
        best_j = len(height) - 1
        best_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            proposal_area = min(height[i], height[j]) * (j - i)
            if proposal_area > best_area:
                best_area = proposal_area
                best_i = i
                best_j = j
            height_i = height[i]
            height_j = height[j]
            if height_i < height_j:
                i += 1
                while height[i] <= height_i and i < j:
                    i += 1
            else:
                j -= 1
                while height[j] <= height_j and i < j:
                    j -= 1
        return best_area

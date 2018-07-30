class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fill_pos = 0
        for num in nums:
            if num != val:
                nums[fill_pos] = num
                fill_pos += 1
        return fill_pos

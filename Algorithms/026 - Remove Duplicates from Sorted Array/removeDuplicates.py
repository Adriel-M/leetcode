class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = None
        orig_len = len(nums)
        for i in range(orig_len):
            curr_index = orig_len - i - 1
            if nums[curr_index] == curr:
                nums.pop(curr_index)
            else:
                curr = nums[curr_index]
        return len(nums)


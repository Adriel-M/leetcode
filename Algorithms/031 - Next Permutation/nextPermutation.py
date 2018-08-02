class Solution:
    def reverse(self, nums, i, j):
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find what to swap
        start_pos = len(nums)
        prev_number = -1
        for _ in range(len(nums) + 1):
            start_pos -= 1
            if start_pos == -1:
                break
            if nums[start_pos] >= prev_number:
                prev_number = nums[start_pos]
            else:
                break
        # reverse
        if start_pos == -1:
            self.reverse(nums, 0, len(nums) - 1)
            return

        end_pos = start_pos + 1
        while end_pos < len(nums):
            if end_pos == len(nums) - 1 or nums[end_pos + 1] <= nums[start_pos]:
                break
            end_pos += 1

        # swap
        tmp = nums[start_pos]
        nums[start_pos] = nums[end_pos]
        nums[end_pos] = tmp

        # reverse
        self.reverse(nums, start_pos + 1, len(nums) - 1)


Solution().nextPermutation([1, 3, 2])

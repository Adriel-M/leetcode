class Solution:
    def swap(self, nums, target):
        while target >= 1 and target <= len(nums) and target != nums[target - 1]:
            temp = nums[target - 1]
            nums[target - 1] = target
            target = temp

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(nums)):
            if nums[i] < 1 and nums[i] > len(nums):
                continue
            self.swap(nums, nums[i])
        for j in range(len(nums)):
            if nums[j] == ret + 1:
                ret = nums[j]
        return ret + 1

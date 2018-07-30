class Solution:
    def binarySearch(self, nums, start, end, target, lower):
        ret = -1
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                ret = mid
                if lower and mid > 0 and nums[mid - 1] == target:
                    end = mid - 1
                elif not lower and mid < len(nums) - 1 and nums[mid + 1] == target:
                    start = mid + 1
                else:
                    break
        return ret

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower = self.binarySearch(nums, 0, len(nums) - 1, target, True)
        if lower == -1:
            return [-1, -1]
        upper = self.binarySearch(nums, lower, len(nums) - 1, target, False)
        return [lower, upper]

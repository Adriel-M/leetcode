class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = nums[i]
            mid_pos = i + 1
            end_pos = len(nums) - 1
            while mid_pos < end_pos:
                mid = nums[mid_pos]
                end = nums[end_pos]
                res = start + mid + end
                if res == 0:
                    ret.add((start, mid, end))
                    if mid == nums[mid_pos + 1]:
                        while mid_pos < end_pos and mid == nums[mid_pos + 1]:
                            mid_pos += 1
                    else:
                        if end == nums[end_pos - 1]:
                            while mid_pos < end_pos and end == nums[end_pos - 1]:
                                end_pos -= 1
                        else:
                            end_pos -= 1
                elif res > 0:
                    if end == nums[end_pos - 1]:
                        while mid_pos < end_pos and end == nums[end_pos - 1]:
                            end_pos -= 1
                    else:
                        end_pos -= 1
                else:
                    if mid == nums[mid_pos + 1]:
                        while mid_pos < end_pos and mid == nums[mid_pos + 1]:
                            mid_pos += 1
                    else:
                        mid_pos += 1
        return list(ret)

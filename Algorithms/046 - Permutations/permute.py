class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        available_nums = set(nums)
        ret = []

        def generate(curr):
            if len(available_nums) == 0:
                ret.append(curr[:])
            else:
                for num in nums:
                    if num in available_nums:
                        available_nums.remove(num)
                        generate(curr + [num])
                        available_nums.add(num)
        generate([])
        return ret

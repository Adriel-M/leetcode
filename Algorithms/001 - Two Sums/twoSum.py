class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # populate lookup table
        num_lookup = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in num_lookup:
                num_lookup[num].append(i)
            else:
                num_lookup[num] = [i]

        # figure out which indices to return
        for j in range(len(nums)):
            anchor_num = nums[j]
            num_to_look_for = target - anchor_num
            # if anchor_num and num_to_look_for are the same
            if anchor_num == num_to_look_for:
                if len(num_lookup[anchor_num]) >= 2:
                    return num_lookup[anchor_num][-2:]
            else:
                if num_to_look_for in num_lookup:
                    return [j, num_lookup[num_to_look_for][0]]


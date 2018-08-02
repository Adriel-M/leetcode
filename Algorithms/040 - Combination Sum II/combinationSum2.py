class Solution:
    def generate(self, candidates, target, curr_count, curr_set, ret):
        if curr_count == target:
            ret.add(tuple(curr_set))
            return
        else:
            for i, num in enumerate(candidates):
                new_sum = curr_count + num
                if new_sum > target:
                    break
                self.generate(
                    candidates[i + 1:], target, new_sum, curr_set + [num], ret)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_candidates = sorted(candidates)
        ret = set()
        self.generate(sorted_candidates, target, 0, [], ret)
        return list(ret)

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        split_s = s.strip().split(' ')
        if len(split_s) == 0:
            return 0
        else:
            return len(split_s[-1])

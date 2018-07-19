class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        split = haystack.split(needle)
        if (len(split) == 1):
            return -1
        else:
            return len(split[0])


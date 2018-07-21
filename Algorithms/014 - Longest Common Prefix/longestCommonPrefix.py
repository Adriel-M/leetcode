class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return
        i = 0
        try:
            while True:
                letters = set()
                for j in range(len(strs)):
                    if j == 0:
                        letters.add(strs[j][i])
                    else:
                        if strs[j][i] not in letters:
                            return strs[0][:i]
                i += 1
        except IndexError:
            pass
        return strs[0][:i]


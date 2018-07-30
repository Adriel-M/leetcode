class Solution:
    def getPalindrome(self, s, i, j):
        good_i = None
        good_j = None
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            else:
                good_i = i
                good_j = j
                i -= 1
                j += 1
        return good_i, good_j

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best_i = None
        best_j = None
        best_len = -1
        if not s:
            return ''
        if s == s[::-1]:
            return s
        # root is on a letter
        for root_start in range(len(s)):
            potential_i, potential_j = self.getPalindrome(
                s, root_start, root_start)
            length = potential_j - potential_i + 1
            if length > best_len:
                best_i = potential_i
                best_j = potential_j
                best_len = length

        for root_start in range(1, len(s)):
            potential_i, potential_j = self.getPalindrome(
                s, root_start - 1, root_start)
            if potential_i is not None and potential_j is not None:
                length = potential_j - potential_i + 1
                if length > best_len:
                    best_i = potential_i
                    best_j = potential_j
                    best_len = length
        if best_i is not None and best_j is not None:
            return s[best_i:best_j + 1]

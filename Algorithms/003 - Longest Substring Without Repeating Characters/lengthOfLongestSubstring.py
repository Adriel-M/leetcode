class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        i = 0
        j = 0
        should_remove = False
        curr_substring = set()
        while i < len(s) and j < len(s):
            if should_remove:
                if s[j] == s[i]:
                    should_remove = False
                    i += 1
                else:
                    curr_substring.remove(s[j])
                j += 1
            else:
                if s[i] in curr_substring:
                    should_remove = True
                else:
                    curr_substring.add(s[i])
                    i += 1
                    if len(curr_substring) > max_length:
                        max_length = len(curr_substring)
        return length

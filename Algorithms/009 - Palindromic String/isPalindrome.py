class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_num = str(x)
        i = 0
        j = len(str_num) - 1
        while i < j:
            if str_num[i] != str_num[j]:
                return False
            i += 1
            j -= 1
        return True

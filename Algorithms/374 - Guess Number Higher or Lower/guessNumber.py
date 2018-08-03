class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i <= j:
            mid = (i + j) // 2
            guessed = guess(mid)
            if guessed == 0:
                return mid
            elif guessed == -1:
                j = mid - 1
            else:
                i = mid + 1
        return -1

class Solution:
    MAX_NUM = (2 ** 31) - 1
    MIN_NUM = -(2 ** 31)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        str_string = str(x).split('-')
        negative = False
        if len(str_string) == 2:
            negative = True
        for i in range(len(str_string[-1])):
            ret += int(str_string[-1][-i - 1]) * \
                (10 ** (len(str_string[-1]) - i - 1))
        if negative:
            ret = -ret
            if ret < self.MIN_NUM:
                return 0
            return ret
        else:
            if ret > self.MAX_NUM:
                return 0
            return ret

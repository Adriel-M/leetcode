class Solution:
    MIN_NUM = -(2 ** 31)
    MAX_NUM = (2 ** 31) - 1
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        negative = 0
        if dividend < 0:
            negative += 1
        if divisor < 0:
            negative += 1
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        orig_abs_divisor = abs_divisor
        sub = 1
        # find max abs_divisor
        while abs_divisor <= abs_dividend:
            prop_divisor = abs_divisor << 1
            if prop_divisor < abs_dividend:
                sub <<= 1
                abs_divisor = prop_divisor
            else:
                break
        while abs_dividend > 0:
            while not abs_divisor <= abs_dividend:
                if abs_divisor == orig_abs_divisor:
                    break
                abs_divisor >>= 1
                sub >>= 1
            abs_dividend -= abs_divisor
            ret += sub
        if abs_dividend < 0:
            ret -= 1
        if negative == 1:
            ret = -ret
            if ret < self.MIN_NUM:
                return self.MAX_NUM
            return ret
        return min(ret, self.MAX_NUM)


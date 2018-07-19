class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        stripped_string = str.strip()
        negative = False
        collected_nums = []
        for i in range(len(stripped_string)):
            if i == 0 and stripped_string[i] == '-':
                negative = True
                continue
            elif i == 0 and stripped_string[i] == '+':
                continue
            if stripped_string[i].isnumeric():
                collected_nums.append(int(stripped_string[i]))
            else:
                break
        ret = 0
        print(collected_nums)
        print(ret)
        for i in range(len(collected_nums)):
            ret += collected_nums[i] * (10 ** (len(collected_nums) - i - 1))
        if negative:
            return max(-1 * ret, -2147483648)
        else:
            return min(ret, 2147483647)


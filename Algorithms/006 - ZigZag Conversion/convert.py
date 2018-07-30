class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            p = []
            placeholder = []
            for _ in range(numRows):
                placeholder.append(p.copy())
            bucket = 0
            down = True
            for i in range(len(s)):
                placeholder[bucket].append(s[i])
                if bucket == 0:
                    down = True
                elif bucket == numRows - 1:
                    down = False
                if down:
                    bucket += 1
                else:
                    bucket -= 1
            ret = ''
            for holder in placeholder:
                ret += ''.join(holder)
            return ret

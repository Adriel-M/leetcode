class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        filtered_s = list(filter(lambda x: x != '-', S))
        start = filtered_s[:len(filtered_s) % K]
        rest = [''.join(filtered_s[i:i + K]) for i in range(len(filtered_s) % K, len(filtered_s), K)]
        if len(start) > 0:
            if len(rest) > 0:
                return ''.join(start).upper() + '-' + '-'.join(rest).upper()
            else:
                return ''.join(start).upper()
        else:
            return '-'.join(rest).upper()


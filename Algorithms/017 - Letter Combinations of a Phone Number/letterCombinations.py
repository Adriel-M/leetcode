class Solution:
    numLetterMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        self.letterHelper(digits, '', ret)
        return ret

    def letterHelper(self, digits, currString, ret):
        if len(digits) == 0:
            return
        if len(digits) == 1:
            for letter in self.numLetterMap[digits[0]]:
                ret.append(currString + letter)
        for letter in self.numLetterMap[digits[0]]:
            self.letterHelper(digits[1:], currString + letter, ret)

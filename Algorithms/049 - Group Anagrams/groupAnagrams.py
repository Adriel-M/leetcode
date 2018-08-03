class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        def hash_string(string):
            ret = 0
            for letter in string:
                ret += hash(letter)
            return ret
        for word in strs:
            hash_val = hash_string(word)
            if hash_val in anagrams:
                anagrams[hash_val].append(word)
            else:
                anagrams[hash_val] = [word]
        ret = []
        for key in anagrams:
            ret.append(anagrams[key])
        return ret

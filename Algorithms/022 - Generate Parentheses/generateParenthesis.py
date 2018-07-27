class Solution:
    def generate(self, n, curr_stack, curr_str, ret, target_len):
      if len(curr_str) == target_len:
        ret.append(curr_str)
        return
      if n > 0:
        self.generate(n - 1, curr_stack + 1, curr_str + '(', ret, target_len)
      for i in range(curr_stack):
        self.generate(n, curr_stack - i - 1, curr_str + ')', ret, target_len)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.generate(n, 0, "", ret, n * 2)
        return ret

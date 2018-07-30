class Solution:
    def isValid(self, s):
        stack = []
        opening_map = {'(': ')', '{': '}', '[': ']'}
        closing_map = {')': '(', '}': '{', ']': '['}
        try:
            for letter in s:
                if letter in opening_map:
                    stack.append(opening_map[letter])
                elif letter in closing_map:
                    if letter != stack.pop():
                        return False
        except IndexError:
            return False
        return len(stack) == 0

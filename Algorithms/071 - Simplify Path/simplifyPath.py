class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []

        def simplify(split, stack):
            if len(split) > 0:
                popped = split.pop()
                if popped == "." or popped == "":
                    simplify(split, stack)
                elif popped == '..':
                    simplify(split, stack + 1)
                else:
                    if stack > 0:
                        simplify(split, stack - 1)
                    else:
                        ret.append(popped)
                        simplify(split, stack)
        simplify(path.split("/"), 0)
        ret.reverse()
        return "/" + "/".join(ret)

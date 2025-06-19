class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        matching = { ')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in matching.values():
                stack.append(char)

            elif char in matching:
             if not stack or stack.pop() != matching[char]:
                    return False
   
        return not stack
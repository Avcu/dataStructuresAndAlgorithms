## Python built-in stacks are used.

from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        
        for idx in range(len(s)):
            ch = s[idx]
            
            # starting char
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            
            # ending char
            elif ch == ")" or ch == "}" or ch == "]":
                if len(stack) == 0:
                    return False
                else:                    
                    popped = stack.pop()
                    if (ch == ")" and popped == "(") or (ch == "}" and popped == "{") or (ch == "]" and popped == "["):
                        continue
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
        return False
"""20.Valid Parentheses

References: https://leetcode.com/problems/valid-parentheses/

"""

__all__ = ['Solution1']


class Solution1:
    """栈"""

    @staticmethod
    def is_valid(s: str) -> bool:
        stack = list()
        for index, char in enumerate(s):
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                top_char = stack.pop()
                if char == ')' and top_char != '(':
                    return False
                if char == ']' and top_char != '[':
                    return False
                if char == '}' and top_char != '{':
                    return False
        return not stack

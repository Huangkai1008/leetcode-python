"""20.Valid Parentheses

References:
    https://leetcode.com/problems/valid-parentheses/
    https://leetcode-cn.com/problems/valid-parentheses/

"""

__all__ = ['Solution1']


class Solution1:
    """栈

    1.先判断字符串的长度是否是偶数，如果不是，肯定无法匹配；
    2.维护一个栈，遍历给定的字符串 `s` ：
      a.当遇到左括号时入栈
      b.当遇到右括号时需要去栈顶找匹配的左括号，如果此时栈中没有元素或者栈顶对应的左括号类型不匹配则返回False
        如果存在匹配则将栈顶元素出栈
    3.遍历结束后如果栈中还存在元素，那么说明没有一一匹配上，返回False

    * 时间复杂度: O(N)，其中N为字符串的长度
    * 空间复杂度: O(N)，其中N为字符串的长度，最坏情况下栈的长度可能等于字符串的长度

    """

    @staticmethod
    def is_valid(s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = list()
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack

"""232. Implement Queue using Stacks

References:
    https://leetcode.com/problems/implement-queue-using-stacks/
    https://leetcode-cn.com/problems/implement-queue-using-stacks/

"""

from collections import deque


class MyQueue:
    """双栈

    定义「输入栈」保存入队（`push`）的元素；
    每次 `pop` 或 `peek` 时，当「输出栈」为空时，输入栈的元素全部倒序压入「输出栈」中

    * 时间复杂度: `push` 和 `empty` 为 O(1), `pop` 和 `peek` 为均摊 O(1)
    * 空间复杂度: O(N)

    """

    def __init__(self):
        self._in_stack = list()
        self._out_stack = list()

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def pop(self) -> int:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack.pop()

    def peek(self) -> int:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack[-1]

    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack


class MyQueue1:
    """使用Python的双端队列实现"""

    def __init__(self):
        self._stack = deque()

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.popleft()

    def peek(self) -> int:
        return self._stack[0]

    def empty(self) -> bool:
        return not self._stack

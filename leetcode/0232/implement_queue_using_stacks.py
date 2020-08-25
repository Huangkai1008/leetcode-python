"""232. Implement Queue using Stacks

References:
    https://leetcode.com/problems/implement-queue-using-stacks/
    https://leetcode-cn.com/problems/implement-queue-using-stacks/

"""


class MyQueue:
    """双栈

    定义「输入栈」保存入队（`push`）的元素；
    每次出队（`pop`）时输入栈的元素全部倒序压入「输出栈」中

    * 时间复杂度: O(N)
    * 空间复杂度: O(N)

    """

    def __init__(self):
        self._in_stack = list()
        self._out_stack = list()

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def pop(self) -> int:
        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())

        val = self._out_stack.pop()
        while self._out_stack:
            self._in_stack.append(self._out_stack.pop())
        return val

    def peek(self) -> int:
        return self._in_stack[0]

    def empty(self) -> bool:
        return not self._in_stack

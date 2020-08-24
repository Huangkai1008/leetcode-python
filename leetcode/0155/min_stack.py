"""155. Min Stack

References:
    https://leetcode.com/problems/min-stack/
    https://leetcode-cn.com/problems/min-stack/

"""


class MinStack:
    """辅助栈

    定义「数据栈」支持`push`、`pop`、`top` 操作
    定义「辅助栈」保持栈顶元素为当前的最小值

    当元素入数据栈时，如果此元素不大于辅助栈的栈顶元素，那么此元素也需要压入辅助栈的栈顶；
    当元素从栈顶被弹出时，如果此元素等于辅助栈的栈顶元素，即此元素就是当前的最小值，也需要从辅助栈弹出

    * 时间复杂度: O(1)
    * 空间复杂度: O(N)，其中`N`为总操作数，最坏情况下，我们会连续插入`N`个元素，此时两个栈占用的空间为 O(N)


    """

    def __init__(self):
        self._stack = list()
        self._min_stack = list()

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop(-1)
        if self._min_stack[-1] == val:
            self._min_stack.pop(-1)

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]

"""如何仅用递归函数和栈操作逆序一个栈

一个栈依次压入 1、2、3、4、5，那么从栈顶到栈底分别为 5、4、3、2、1。
将这个栈转置后，从栈顶到栈底为 1、2、3、4、5，也就是实现栈中元素的逆序。

Notes: 只能用递归函数来实现，不能用其他数据结构。

"""
from typing import List


def reverse_in_place(stack: List[int]) -> None:
    """
    >>> s = [1, 2, 3, 4, 5]
    >>> reverse_in_place(s)
    >>> s
    [5, 4, 3, 2, 1]
    """
    if not stack:
        return

    e = get_and_remove_last_element(stack)
    reverse_in_place(stack)
    stack.append(e)


def get_and_remove_last_element(stack: List[int]) -> int:
    """将栈底的元素返回并移除
    >>> s = [1, 2, 3, 4, 5]
    >>> e = get_and_remove_last_element(s)
    >>> e
    1
    >>> s
    [2, 3, 4, 5]
    """
    r = stack.pop()
    if not stack:
        return r

    last = get_and_remove_last_element(stack)
    stack.append(r)
    return last


def reverse(stack: List[int]) -> List[int]:
    """
    >>> s = [1, 2, 3, 4, 5]
    >>> reverse(s)
    [5, 4, 3, 2, 1]
    """
    if not stack:
        return []

    return [stack.pop()] + reverse(stack)

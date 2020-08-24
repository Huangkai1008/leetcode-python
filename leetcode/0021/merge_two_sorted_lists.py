"""21. Merge Two Sorted Lists

References:
    https://leetcode.com/problems/merge-two-sorted-lists/
    https://leetcode-cn.com/problems/merge-two-sorted-lists/

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution1:
    """迭代

    判断哪一个链表的头节点的值更小，将较小值的节点添加到结果里
    当一个节点被添加到结果里之后，将对应链表中的节点向后移一位

    增加一个「虚拟头节点(`dummy node`)」 / 「哨兵节点(sentinel node)」
    可以使返回合并后的结果更加简单

    * 时间复杂度: O(n+m)，其中 `n` 和 `m` 分别为两个链表的长度
    * 空间复杂度: O(1)

    """
    @staticmethod
    def merge_two_lists(
        list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = cur = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 is not None:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next

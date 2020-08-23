"""237.Delete Node in a Linked List

References:
    https://leetcode.com/problems/delete-node-in-a-linked-list/
    https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

"""
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None


class Solution1:
    """

    将后一节点的值复制给待删除节点，然后将后一节点当作「待删除节点」来进行删除

    * 时间复杂度: O(1)
    * 空间复杂度: O(1)

    """

    @staticmethod
    def delete_node(node: ListNode):
        node.val = node.next.val
        node.next = node.next.next

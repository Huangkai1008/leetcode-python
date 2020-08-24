"""217. Contains Duplicate

References:
    https://leetcode.com/problems/contains-duplicate/
    https://leetcode-cn.com/problems/contains-duplicate/

"""
from typing import List


class Solution:
    """哈希表/集合

    创建一个哈希表，遍历数组的每一个数
    判断元素是否在哈希表中，如果不存在那么将此元素插入到容器中，否则说明存在重复的元素

    * 时间复杂度: O(N)，其中N为数组中的元素数量
    * 空间复杂度: O(N)，其中N为数组中的元素数量，主要为创建哈希表的开销

    """
    @classmethod
    def contains_duplicate(cls, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True

            s.add(num)
        return False

"""1.Two Sum

References:
    https://leetcode.com/problems/two-sum/
    https://leetcode-cn.com/problems/two-sum/

"""

from typing import List

__all__ = ['Solution1', 'Solution2']


class Solution1:
    """暴力枚举

    枚举数组中的每一个数 `x` 和其后的每一个数 `y` ，当`x`和`y`之和满足条件时即返回

    * 时间复杂度: O(N^2)，其中N为数组中的元素数量
    * 空间复杂度: O(1)

    """

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        >>> Solution1.two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> Solution1.two_sum([3, 2, 4], 6)
        [1, 2]

        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return list()


class Solution2:
    """哈希表

    创建一个哈希表，遍历数组中的每一个数 `x`
    判断 `target - x` 是否在哈希表中：
        1. 如果在那么直接返回；
        2. 如果不存在将 `x` 的值作为key, `x`在数组中的位置 `index` 作为value存入哈希表中
    这样可以将每个找 `target - x` 的时间复杂度降到O(1)级别

    * 时间复杂度: O(N)，其中N为数组中的元素数量
    * 空间复杂度: O(N)，其中N为数组中的元素数量，主要为创建哈希表的开销

    """

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        >>> Solution1.two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> Solution1.two_sum([3, 2, 4], 6)
        [1, 2]
        """
        d = dict()
        for index, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], index]
            d[num] = index
        return list()

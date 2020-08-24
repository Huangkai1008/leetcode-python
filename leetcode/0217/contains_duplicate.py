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


class Solution1:
    """排序

    在对数字从小到大排序之后，数组的重复元素一定出现在相邻位置中
    遍历已排序的数组，判断相邻的两个元素是否相等，如果相等则说明存在重复的元素

    * 时间复杂度: O(NlogN)，其中N为数组中的元素数量，需要对数组进行排序
    * 空间复杂度: O(logN)，其中N为数组中的元素数量

    """

    @classmethod
    def contains_duplicate(cls, nums: List[int]) -> bool:
        nums.sort()
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
        return False

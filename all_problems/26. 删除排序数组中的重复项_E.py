#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
26. 删除排序数组中的重复项
"""

"""
题目：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。


你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""
思路1：
弹出重复的元素
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """执行用时: 764 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了21.78% 的用户"""

        if not nums:
            return 0

        i = 1
        while nums[i:]:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return i


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """执行用时: 136 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了27.67% 的用户"""

        if not nums:
            return 0

        i = 1
        try:
            while 1:
                if nums[i] == nums[i - 1]:
                    nums.pop(i)
                else:
                    i += 1

        finally:
            return i


"""
思路2：
遍历元素，将不重复的值复制到前n个元素
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """执行用时: 72 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了99.60% 的用户 """

        if not nums:
            return 0

        n = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[n + 1] = nums[i]
                n += 1

        return n + 1


if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, -1, 0, 1, 1, 2]
    print(nums[:s.removeDuplicates(nums)])

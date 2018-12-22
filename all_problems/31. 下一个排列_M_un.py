#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
31. 下一个排列
"""

"""
题目：
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

"""
思路1：

"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []

        l = len(nums)
        for i in range(l):
            p = l - i - 1
            q = l - i - 2
            if nums[p] > nums[q]:
                nums[p], nums[q] = nums[q], nums[p]
                return

        nums.sort()


if __name__ == '__main__':
    slt = Solution()
    print(slt.nextPermutation([1,2,3]))

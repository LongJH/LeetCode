#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
81. 搜索旋转排序数组 II
"""

"""
题目：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

进阶
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""

"""
思路1：
内置函数
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        """执行用时: 48 ms, 在Search in Rotated Sorted Array II的Python3提交中击败了99.46% 的用户"""
        return target in nums


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """执行用时: 44 ms"""
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == '__main__':
    slt = Solution()
    print(slt.search([4,5,6,7,0,1,2], 0))

import pandas as pd
pd.crosstab(pd.Series([1,2,3,4,5]), pd.Series([1,0,1,0,1]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
31. 下一个排列
"""

"""
题目：
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

"""
思路1：
遍历元组
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """执行用时: 48 ms, 在Find First and Last Position of Element in Sorted Array的Python3提交中击败了99.38% 的用户"""
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                j = i
                for j in range(i + 1, l):
                    if nums[j] != target:
                        return [i, j - 1]

                return [i, j]
        return [-1, -1]


if __name__ == '__main__':
    slt = Solution()
    print(slt.searchRange([2, 2], 2))

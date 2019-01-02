#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
75. 颜色分类
"""

"""
题目：
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

"""
思路：
内置函数
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """执行用时: 44 ms, 在Sort Colors的Python3提交中击败了99.58% 的用户"""
        nums.sort()


"""
思路：
一遍扫描记录个数
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """执行用时: 44 ms, 在Sort Colors的Python3提交中击败了99.58% 的用户 """
        r = w = b = 0
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                w += 1
            else:
                b += 1

        nums[0:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b


if __name__ == '__main__':
    slt = Solution()
    colors = []
    slt.sortColors(colors)
    print(colors)

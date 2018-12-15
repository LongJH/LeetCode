#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
1.两数之和
"""

"""
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

"""
解题思路：
1. 使用哈希表（<键，值>），读取数据（xi）时将当前值所需余数（yi=target-xi）存在“键”中，当前值的位置存在“值”中（即<yi:i>）。
2. 若后续发现有数值与表中某个“键”相等（xj=yi），则表示该数值与这个“值”对应位置的数值相加即为target（xi+xj=target）。
3. 返回 [i, j]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, xi in enumerate(nums):
            if xi in d.keys():
                return [d[xi], i]  # 步骤 2
            else:
                d[target - xi] = i  # 步骤 1
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))

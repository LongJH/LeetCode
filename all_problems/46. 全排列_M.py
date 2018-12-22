#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
46. 全排列
"""

"""
题目：
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
思路1：
内置函数
"""

import itertools
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 56 ms, 在Permutations的Python3提交中击败了99.34% 的用户"""
        return list(itertools.permutations(nums))



if __name__ == '__main__':
    slt = Solution()
    print(slt.permute([1,2,3]))

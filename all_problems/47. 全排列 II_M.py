#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
46. 全排列
"""

"""
题目：
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

"""
思路1：
内置函数
"""

import itertools
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 88 ms, 在Permutations II的Python3提交中击败了96.85% 的用户"""
        return list(set(itertools.permutations(nums)))



if __name__ == '__main__':
    slt = Solution()
    print(slt.permuteUnique([1,1,3]))

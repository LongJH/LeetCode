#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
78. 子集
"""

"""
题目：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

"""
思路：
递归实现
"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 48 ms, 在Subsets的Python3提交中击败了98.64% 的用户"""
        self.nums = nums
        self.res_list = []
        self.subsetsDfs(self.nums, [])

        return self.res_list

    def subsetsDfs(self, nums, res):
        self.res_list.append(res)

        if not nums:
            return

        for i, n in enumerate(nums):
            self.subsetsDfs(nums[i + 1:], res + [n])


if __name__ == '__main__':
    slt = Solution()
    print(slt.subsets([1,2,3]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
77. 组合
"""

"""
题目：
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

"""
思路：
内置函数
"""

from itertools import combinations
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """执行用时: 180 ms, 在Combinations的Python3提交中击败了79.76% 的用户"""
        return list(combinations(range(1, n+1), k))


"""
思路：
递归实现
"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """执行用时: 172 ms, 在Combinations的Python3提交中击败了82.14% 的用户"""
        self.nums = list(range(1, n+1))
        self.res_list = []
        self.combineDfs(self.nums, k, [])

        return self.res_list

    def combineDfs(self, nums, k, res):
        if not k:
            self.res_list.append(res)

        for i, n in enumerate(nums[:len(nums) - k + 1]):
            self.combineDfs(nums[i + 1:], k - 1, res + [n])


if __name__ == '__main__':
    slt = Solution()
    print(slt.combine(4, 2))

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

"""
思路2：
深度递归
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 100 ms, 在Permutations的Python3提交中击败了10.57% 的用户"""
        self.res_list = []
        res = []
        self.permuteDfs(nums, res)
        return self.res_list


    def permuteDfs(self, nums, res):
        len_nums = len(nums)
        if len_nums == 1:
            self.res_list.append(res + nums)
            return

        for i in range(len_nums):
            nums2 = nums.copy()
            del nums2[i]
            self.permuteDfs(nums2, res + [nums[i]])

"""
思路3：
广度遍历
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 56 ms, 在Permutations的Python3提交中击败了99.29% 的用户"""
        len_nums = len(nums)
        if not len_nums:
            return [[]]
        if len_nums == 1:
            return [nums]

        res_list = []
        res1 = self.permute(nums[1:])
        # print(res1)
        # 取出第一位 插入到 res 中每个结果的每两个元素之间
        n = nums[0]
        for res in res1:
            for j in range(len_nums):
                res_list.append(res[:j] + [n] + res[j:])

        return res_list




if __name__ == '__main__':
    slt = Solution()
    print(slt.permute([1,2,3]))
l = [1,2,3]
l2 = l
l.pop()
l2
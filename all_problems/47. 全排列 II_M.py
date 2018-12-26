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


"""
思路2：
广度遍历
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 76 ms, 在Permutations II的Python3提交中击败了99.35% 的用户"""
        len_nums = len(nums)
        if not len_nums:
            return [[]]
        if len_nums == 1:
            return [nums]

        res_list = []
        res1 = self.permuteUnique(nums[1:])
        # print(res1)
        # 取出第一位 插入到 res 中每个结果的每两个元素之间
        n = nums[0]
        for res in res1:
            for j in range(len_nums):
                res_list.append(res[:j] + [n] + res[j:])
                if j < len_nums - 1 and res[j] == n:        # 关键：但 res[j] == n 时即可跳出遍历，若继续遍历会出现重复
                    break

        return list(res_list)


if __name__ == '__main__':
    slt = Solution()
    print(slt.permuteUnique([1,1,2]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
39. 组合总和
"""

"""
题目：
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

"""
解题思路：
递归
让 target 减去数组中每个元素。
若结果 >0 ，则在原数组中寻找和为 target - i 的组合
若结果 =0 ，则在结果集合中加上当前的结果
若结果 <0 ，表示以后的元素都大于当前 target，直接返回
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """执行用时: 104 ms, 在Combination Sum的Python3提交中击败了68.19% 的用户"""
        res_list = []
        candidates.sort()
        self.combination(candidates, target, res_list, [])
        return res_list

    def combination(self, candidates, target, res_list, res):
        if not candidates:
            return

        for i, n in enumerate(candidates):
            new_t = target - n
            new_res = res + [n]
            if new_t == 0:
                res_list.append(new_res)
            elif new_t > 0:
                self.combination(candidates[i:], target - n, res_list, new_res)
            else:
                return


"""
优化：
减少 res 的赋值以及参数的传递
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """执行用时: 72 ms, 在Combination Sum的Python3提交中击败了99.70% 的用户"""
        self.res_list = []
        self.candidates = sorted(candidates)
        self.combination(target, [], 0)
        return self.res_list

    def combination(self, target, res, i):
        while i < len(self.candidates):
            n = self.candidates[i]
            new_t = target - n
            if new_t == 0:
                self.res_list.append(res + [n])
            elif new_t > 0:
                self.combination(new_t, res + [n], i)
            else:
                return
            i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))

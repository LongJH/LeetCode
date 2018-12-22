#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
40. 组合总和 II
"""

"""
题目：
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""

"""
解题思路：
递归, 同 39. 组合总和, 
让 target 减去数组中每个元素。
若结果 >0 ，则在剔除该元素的数组中寻找和为 target - i 的组合
若结果 =0 ，则在结果集合中加上当前的结果
若结果 <0 ，表示以后的元素都大于当前 target，直接返回
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """执行用时: 60 ms, 在Combination Sum II的Python3提交中击败了99.70% 的用户"""
        self.res_list = []
        self.candidates = sorted(candidates)
        self.combination(target, [], 0)
        return self.res_list

    def combination(self, target, res, j):
        i = j
        while i < len(self.candidates):
            if i > j and self.candidates[i - 1] == self.candidates[i]:
                i += 1
                continue
            n = self.candidates[i]
            new_t = target - n
            if new_t == 0:
                self.res_list.append(res + [n])
            elif new_t > 0:
                self.combination(new_t, res + [n], i + 1)
            else:
                return
            i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))

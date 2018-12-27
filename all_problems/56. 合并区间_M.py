#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
56. 合并区间
"""

"""
题目：
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
解题思路：
每一个新增的元组都与结果的每一个进行对比，若发现重叠，则将旧区间删除并加上新区间
"""


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        """执行用时: 124 ms, 在Merge Intervals的Python3提交中击败了17.25% 的用户"""
        res = []
        for i in intervals:
            tmp = i
            for j in list(res):
                if tmp.start > j.end or tmp.end < j.start:
                    continue
                tmp.start = tmp.start if tmp.start < j.start else j.start
                tmp.end = tmp.end if tmp.end > j.end else j.end
                res.remove(j)
            res.append(tmp)

        return res


"""
解题思路：
先将 intervals 按start排序，再逐个判断右区间
"""

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        """执行用时: 72 ms, 在Merge Intervals的Python3提交中击败了99.50% 的用户"""
        res = []

        intervals.sort(key=lambda a: a.start)
        for i in intervals:
            if not res or i.start > res[-1].end:
                res.append(i)
                continue

            res[-1].end = max(res[-1].end, i.end)


        return res


if __name__ == '__main__':
    s = Solution()
    intrls = [Interval(1, 2), Interval(3, 4), Interval(8, 9), Interval(0, 5)]
    print([[i.start, i.end] for i in s.merge(intrls)])


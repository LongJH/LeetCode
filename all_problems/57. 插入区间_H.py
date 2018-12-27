#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
56. 合并区间
"""

"""
题目：
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]

示例 2:
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
解题思路：
参考 56. 合并区间
"""


class Solution:

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        """执行用时: 68 ms, 在Insert Interval的Python3提交中击败了98.54% 的用户"""
        return self.merge(intervals + newInterval)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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
    new_intrls = [Interval(3, 7)]
    print([[i.start, i.end] for i in s.insert(intrls, new_intrls)])


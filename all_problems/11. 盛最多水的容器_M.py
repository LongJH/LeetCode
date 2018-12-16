#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
11. 盛最多水的容器
"""

"""
题目：
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""

"""
解题思路：
暴力法
1. 求出每个 i j 对应的容量
2. 求最大值
复杂度 O(n^2)
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """超出时间限制"""
        if len(height) <= 1:
            return 0

        max_area = 0
        for i, hi in enumerate(height):
            for j, hj in enumerate(height[i:], i):
                max_area = max(max_area, min(hi, hj) * (j - i))

        return max_area


"""
解题思路2：
双指针法
1. 容量取决于最短高度的一侧，故取两个指针分别从最前与最后开始往中间靠拢，每次移动高度较短的指针
2. 每次移动计算容量，求最大值
只需要进行一次遍历，复杂度 O(n)
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """执行用时: 84 ms, 在Container With Most Water的Python3提交中击败了78.00% 的用户"""
        i, j = 0, len(height) - 1   # 前后指针
        if j <= 0:
            return 0

        max_area = 0
        while i != j:
            hi = height[i]
            hj = height[j]
            max_area = max(max_area, min(hi, hj) * (j - i))
            if hi <= hj:
                i += 1
            else:
                j -= 1

        return max_area

"""
解题思路3：
双指针法基础上增加 max_h， 若 max_h * (j - i) < max_area 提前退出
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """执行用时: 68 ms, 在Container With Most Water的Python3提交中击败了97.24% 的用户"""
        i, j = 0, len(height) - 1   # 前后指针
        if j <= 0:
            return 0

        max_h = max(height)
        max_area = 0
        while i != j:
            hi = height[i]
            hj = height[j]
            d = j - i

            if max_h * d <= max_area:
                break

            max_area = max(max_area, min(hi, hj) * d)
            if hi <= hj:
                i += 1
            else:
                j -= 1

        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

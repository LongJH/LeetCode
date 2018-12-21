#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
42. 接雨水
"""

"""
题目：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

"""
解题思路：
双指针法
1. 容量凹槽部分，故取两个指针分别从最前与最后开始往中间靠拢，每次移动高度较短的指针
2. 每次移动计算容量，求最大值
只需要进行一次遍历，复杂度 O(n)
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """执行用时: 72 ms, 在Trapping Rain Water的Python3提交中击败了43.22% 的用户"""
        i, j = 0, len(height) - 1   # 前后指针
        if j <= 0:
            return 0

        m_l = height[i]
        m_r = height[j]
        all_area = l_area = r_area = 0     # 用于存放当前水槽容量
        while i != j:
            if i == len(height) - 1 or j == 0:
                break

            print(m_l, height[i], height[j], m_r, l_area, r_area)
            if m_l <= m_r:      # 移动左指针
                i += 1
                if height[i] < m_l:
                    l_area += (m_l - height[i])
                    print(l_area)
                else:
                    m_l = height[i]
                    all_area += l_area
                    l_area = 0
            else:               # 移动右边指针
                j -= 1
                if height[j] < m_r:
                    r_area += (m_r - height[j])
                else:
                    m_r = height[j]
                    all_area += r_area
                    r_area = 0

        return all_area


if __name__ == '__main__':
    s = Solution()
    print(s.trap([1,2,2,2]))

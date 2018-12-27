#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
53. 最大子序和
"""

"""
题目：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

"""
解题思路：
使用 tmp 表示当前的和，m 表示最大值
从第一个元素开始往后遍历，若 tmp < 0 则令 tmp=0，然后 tmp += i
若 m = max(tmp, m)
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """执行用时: 56 ms, 在Maximum Subarray的Python3提交中击败了91.19% 的用户"""
        m = nums[0]
        tmp = 0

        for i in nums:
            if tmp < 0:
                tmp = 0
            tmp += i

            m = max(m, tmp)

        return m


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([1,2,3]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
69. x 的平方根
"""

"""
题目：
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""

"""
解题思路：
使用二分法查找
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """执行用时: 96 ms, 在Sqrt(x)的Python3提交中击败了32.16% 的用户"""
        if x == 0 or x == 1:
            return x

        l = 0
        r = x

        while l < r - 1:
            print(l, r)
            n = (l + r) // 2
            n2 = n ** 2

            if n2 > x:
                r = n
            else:
                l = n

        return (l + r) // 2


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """执行用时: 68 ms, 在Sqrt(x)的Python3提交中击败了91.65% 的用户"""
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """执行用时: 68 ms, 在Sqrt(x)的Python3提交中击败了91.65% 的用户"""
        return int(x ** 0.5)

if __name__ == '__main__':
    slt = Solution()
    print(slt.mySqrt(9))

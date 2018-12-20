#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
29. 两数相除
"""


"""
题目：
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""

"""
思路：
内置函数实现
"""


class Solution:
    max_num = 2 ** 31 - 1
    min_num = - 2 ** 31
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """执行用时: 60 ms, 在Divide Two Integers的Python3提交中击败了99.50% 的用户"""
        flag = -1 if (dividend > 0) ^ (divisor > 0) else 1
        res = flag * (abs(dividend) // abs(divisor))
        return res if res < self.max_num else self.max_num


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-7, 3))
abs(-7) // abs(3)
True ^ True

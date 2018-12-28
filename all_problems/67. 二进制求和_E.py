#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
67. 二进制求和
"""

"""
题目：
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""

"""
解题思路：
从后到前依次加1
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """执行用时: 48 ms, 在Add Binary的Python3提交中击败了99.72% 的用户"""
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    slt = Solution()
    print(slt.addBinary([9,9,9,9]))

a = "10010"
b = "10010"
int(a, 2)

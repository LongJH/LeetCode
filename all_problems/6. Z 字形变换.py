#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
6. Z 字形变换
"""

"""
题目：
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

"""
解题思路：
1. 先构建一个 n 个空字符的列表，存放各行字符串
2. 用 z 记录变换顺序（1表示往前，-1表示往后），依次遍历字符，往第 i 个列表元素添加字符，当 i 触碰 0 或 n 时使 z 反向
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        s_list = [''] * numRows

        z = 1       # 记录 Z 变换方向
        i = 0       # 记录存在第 i 个列表
        for l in s:
            s_list[i] += l
            i += z
            if i == 0:
                z = 1
            if i == numRows - 1:
                z = -1

        return ''.join(s_list)


if __name__ == '__main__':
    s = Solution()
    print(s.convert("ab", 1))

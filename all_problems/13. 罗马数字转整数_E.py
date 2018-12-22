#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
13. 罗马数字转整数
"""

"""
题目：
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

"""
思路：
从右到左对罗马数字字符进行遍历，若当前数值比前一位大则加上对应数值，若小，则减去对应数值
"""


class Solution:
    def romanToInt(self, s):
        """
        :type num: int
        :rtype: str
        """
        """执行用时: 164 ms, 在Roman to Integer的Python3提交中击败了80.34% 的用户"""
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}

        n = 0
        rev_s = s[::-1]
        for i, l in enumerate(rev_s):
            n_l = mapping[l]
            if i >= 1 and n_l < mapping[rev_s[i - 1]]:
                n -= n_l
            else:
                n += n_l

        return n


"""
思路2：
利用 last 记录上一个数值，可减少 比较次数
"""


class Solution:
    def romanToInt(self, s):
        """
        :type num: int
        :rtype: str
        """
        """执行用时: 160 ms, 在Roman to Integer的Python3提交中击败了82.44% 的用户"""
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}

        n = 0
        last = 0
        for l in s[::-1]:
            n_l = mapping[l]
            if n_l < last:
                n -= n_l
            else:
                n += n_l

            last = n_l

        return n


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))

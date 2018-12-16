#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
9. 回文数
"""

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""

"""
解题思路：
转换字符判断倒序
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """执行用时: 276 ms, 在Palindrome Number的Python3提交中击败了99.79% 的用户"""
        s = str(x)
        return s == s[::-1]


"""
解题思路-进阶：
不转换字符
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """执行用时: 348 ms, 在Palindrome Number的Python3提交中击败了75.56% 的用户"""
        if x < 0:
            return False

        pos_x = x
        rev_x = 0

        while x:    # 当 x>0
            a = x % 10  # 当前 x 个位数
            rev_x = rev_x * 10 + a
            x = x // 10

        return pos_x == rev_x


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-12321))

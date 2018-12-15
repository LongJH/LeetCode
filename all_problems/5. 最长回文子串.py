#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
5. 最长回文子串
"""

"""
题目：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""

"""
解题思路1：
若子串是回文，则子串两侧互为镜像，即从子串中心展开，左右字符依次相等。
例 "abcba" 中心为 "c", "abccba" 中心为 "cc", 若 s 长度为 n 即共可以找到 2n-1 个中心
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 452 ms, 在Longest Palindromic Substring的Python3提交中击败了69.05% 的用户 """

        s_len = len(s)

        if s_len <= 1 or s == s[::-1]:
            return s

        max_sub = s[0]  # 记录最大回文子串

        # 寻找单中心
        for i in range(1, s_len):
            # 寻找单中心
            j = 1
            while j < min(i + 1, s_len - i):
                if s[i - j] != s[i + j]:
                    break
                j += 1

            t_sub = s[i - j + 1: i + j]
            max_sub = t_sub if len(t_sub) > len(max_sub) else max_sub

            # 双中心
            if s[i - 1] == s[i]:
                j = 1
                while j < min(i, s_len - i):
                    if s[i - j - 1] != s[i + j]:
                        break
                    j += 1

                t_sub = s[i - j: i + j]
                max_sub = t_sub if len(t_sub) > len(max_sub) else max_sub

        return max_sub


"""
思路2：
使用max_len记录目前最大的回文串长度，对以后每一个字符，将其作为末端判断长度为 max_len + 1 的子串是否回文串
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 68 ms, 在Longest Palindromic Substring的Python3提交中击败了100.00% 的用户 """

        s_len = len(s)

        if s_len <= 1 or s == s[::-1]:
            return s

        max_len = 1  # 记录最大回文子串长度
        start = 0  # 记录最大回文子串开始位置

        for i in range(1, s_len):
            odd = s[i - max_len - 1: i + 1]  # 奇数长度
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue

            even = s[i - max_len: i + 1]  # 偶数长度
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        return s[start: start + max_len]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("acdcc"))
    "acc"[-2:0]

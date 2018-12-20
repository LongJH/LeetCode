#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
28. 实现strStr()
"""

"""
题目：
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""

"""
思路1：

"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """执行用时: 40 ms, 在Implement strStr()的Python3提交中击败了99.74% 的用户"""
        if not needle:
            return 0

        for n in range(len(haystack) - len(needle) + 1):
            if haystack[n:].startswith(needle):
                return n

        return -1


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """执行用时: 40 ms, 在Implement strStr()的Python3提交中击败了99.74% 的用户"""
        if not needle:
            return 0

        l2 = len(needle)
        for n in range(len(haystack) - l2 + 1):
            if haystack[n:n+l2] == needle :
                return n

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hell", "ll"))

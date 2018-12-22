#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
14. 最长公共前缀
"""

"""
题目：
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""

"""
解题思路：
依次判断每个字符是否在各字符串对应位置，若不一样，抛出异常，最终返回公共字段块
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """执行用时: 44 ms, 在Longest Common Prefix的Python3提交中击败了99.65% 的用户"""
        if not strs or "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        com = ''
        try:
            for i, l in enumerate(strs[0]):
                for other_s in strs[1:]:
                    if other_s[i] != l:
                        raise ValueError
                com += l
        finally:
            return com


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["","flow","flight"]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
58. 最后一个单词的长度
"""

"""
题目：
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
"""

"""
解题思路：

"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 44 ms, 在Length of Last Word的Python3提交中击败了89.75% 的用户"""
        return len(s.split()[-1]) if s.split() else 0

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))

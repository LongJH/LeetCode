#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
71. 简化路径
"""

"""
题目：
给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
"""

"""
解题思路1：
将路径按 / 切割，逐个遍历，若是 . 则删除，若是 .. 则删除上一层
"""


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """执行用时: 48 ms, 在Simplify Path的Python3提交中击败了98.82% 的用户"""
        s_path = []
        for l in path.split('/'):
            if not l or l == '.':
                continue

            if l != '..':
                s_path.append(l)
            elif s_path:
                s_path.pop()

        return '/' + '/'.join(s_path)


if __name__ == '__main__':
    slt = Solution()
    print(slt.simplifyPath("/././../../../c/"))
[].pop()
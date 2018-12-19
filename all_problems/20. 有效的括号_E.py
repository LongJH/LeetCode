#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
8. 字符串转换整数 (atoi)
"""

"""
题目：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

"""
解题思路：
使用栈结构，若栈
"""


class Solution:
    left = ["(", "[", "{"]
    right = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """执行用时: 44 ms, 在Valid Parentheses的Python3提交中击败了99.32% 的用户"""
        stack = []
        for l in s:
            if l in self.left:
                stack.append(l)
                continue

            try:
                if l == ' ' or self.right[l] == stack.pop():
                    continue
                else:
                    return False
            except:
                return False

        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{[]}}}"))

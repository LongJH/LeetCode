#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
22. 括号生成
"""

"""
题目：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

"""
思路1：
使用递归进行深度搜索
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """执行用时: 56 ms, 在Generate Parentheses的Python3提交中击败了55.28% 的用户"""
        if not n:
            return [""]

        left = right = n        # 用于记录左右括号数量
        string = ""
        res = []
        self.generateDfs(left, right, string, res)
        return res

    def generateDfs(self, left, right, string, res):
        if not left and not right:
            res.append(string)
            return

        if left:                # 剩余左括号
            self.generateDfs(left - 1, right, string + "(", res)
        if right > left:        # 剩余右括号比左括号多
            self.generateDfs(left, right - 1, string + ")", res)


"""
思路2：
使用迭代进行广度搜索
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """执行用时: 56 ms, 在Generate Parentheses的Python3提交中击败了55.28% 的用户"""

        if not n:
            return [""]

        level = 2 * n
        res = [""]

        while level:
            res2 = []
            for r in res:
                left = right = 0
                for i in r:         # 统计当前字符中 左右括号数量
                    if i == "(":
                        left += 1
                    else:
                        right += 1
                if left < n:
                    res2.append(r + "(")
                if left > right:
                    res2.append(r + ")")

            res = res2
            level -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

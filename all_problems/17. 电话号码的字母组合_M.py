#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
17. 电话号码的字母组合
"""

"""
题目：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""

"""
解题思路：

"""


class Solution:
    mapping = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}
    def letterCombinations(self, d):
        """
        :type digits: str
        :rtype: List[str]
        """
        """执行用时: 56 ms, 在Letter Combinations of a Phone Number的Python3提交中击败了16.14% 的用户"""
        if not d:
            return []

        d = list(d)
        res = [""]
        while d:
            l = self.mapping[d.pop(0)]
            res2 = []
            for r in res:
                for i in l:
                    res2.append(r+i)
            res = res2

        return res


"""
使用列表生成式
"""


class Solution:
    mapping = {"0": " ", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def letterCombinations(self, d):
        """
        :type digits: str
        :rtype: List[str]
        """
        """执行用时: 40 ms, 在Letter Combinations of a Phone Number的Python3提交中击败了99.63% 的用户"""
        if not d:
            return []

        res = [""]
        for n in d:
            res = [r + i for r in res for i in self.mapping[n]]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
38. 报数
"""

"""
题目：
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""

"""
思路1：
新建一个方法计算得出下一个字符串
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """执行用时: 56 ms, 在Count and Say的Python3提交中击败了53.05% 的用户"""
        res = '1'

        while n > 1:
            res = self.say(res)
            n -= 1

        return res

    def say(self, s):
        ans = ""
        n, i = 0, s[0]
        for l in s:
            if l == i:
                n += 1
            else:
                ans += str(n) + i
                n = 1
                i = l

        ans += str(n) + i
        return ans



"""
思路2：
使用递归实现
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """执行用时: 44 ms, 在Count and Say的Python3提交中击败了99.27% 的用户"""
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        ans = ""
        n, i = 0, s[0]
        for l in s:
            if l == i:
                n += 1
            else:
                ans += str(n) + i
                n = 1
                i = l

        ans += str(n) + i
        return ans


if __name__ == '__main__':
    slt = Solution()
    print(slt.countAndSay(5))

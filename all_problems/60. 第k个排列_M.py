#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
60. 第k个排列
"""

"""
题目：
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"
"""

"""
思路1：
内置函数
"""


import itertools
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """执行用时: 852 ms, 在Permutation Sequence的Python3提交中击败了2.32% 的用户"""
        nums = list(map(str, range(1, n + 1)))
        prmt = itertools.permutations(nums)
        i = 1
        while 1:
            if i == k:
                return "".join(prmt.__next__())
            next(prmt)
            i += 1


"""
思路2：
[1,2,3,…,n]所组成的排列一共有 n! 种，若将所有排列先列出效率太低。
由于给出的数值是从小到大排列，若给定 k，从假设 k-1 / (n-1)! = a1 余 b1，则可以判定生成的第一位列表中第 a1 个元素(a1+1)
确定第一位后，在列表中把 第 a1 个元素去掉，再通过 b1 / (n-1)! = a2 余 b2, 可以确定第二位元素。
依次类推，即可以得出结果。
"""


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """执行用时: 56 ms, 在Permutation Sequence的Python3提交中击败了46.64% 的用户"""
        """使用//和%替代divmod，执行用时: 44 ms, 在Permutation Sequence的Python3提交中击败了98.84% 的用户"""
        num_list = list(map(str, range(1, n + 1)))
        k = k - 1
        res = ''

        # p = 1
        # for i in range(1, 10):
        #     p *= i
        #     print(p, end=',')
        per_list = [1,1,2,6,24,120,720,5040,40320,362880]   # 对应每个n-1下面阶乘

        while n:
            n -= 1
            a = k // per_list[n]
            # a, b = divmod(k, per_list[n])
            res += num_list.pop(a)
            k %= per_list[n]

        return res


if __name__ == '__main__':
    slt = Solution()
    print(slt.getPermutation(9, 161191))

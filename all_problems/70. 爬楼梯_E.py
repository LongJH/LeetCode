#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
70. 爬楼梯
"""

"""
题目：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

"""
解题思路：
n阶结果等于n-1阶加上n-2阶，可构造一个斐波那契数列求解
1. 递归
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """超出时间限制"""
        if n == 1 or n == 0:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """执行用时: 48 ms, 在Climbing Stairs的Python3提交中击败了46.79% 的用户"""
        if n == 1 or n == 0:
            return 1

        a, b = 1, 1
        for i in range(n-1):
            a, b = a+b, a

        return a


"""
解题思路：
n阶结果等于n-1阶加上n-2阶，可构造一个斐波那契数列求解
2. 使用通项公式
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """执行用时: 48 ms, 在Climbing Stairs的Python3提交中击败了46.79% 的用户"""
        return round(1 / (5 ** 0.5) * (((1 + 5 ** 0.5)/2)**(n+1) + ((1 - 5 ** 0.5)/2)**(n+1)))


if __name__ == '__main__':
    slt = Solution()
    print(slt.climbStairs(9))
5 ** 0.5
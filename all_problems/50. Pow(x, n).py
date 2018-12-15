#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
50. Pow(x, n)
"""

"""
题目：
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2^-2 = 1/2^2 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
"""

"""
思路：
使用递归实现，如果每次只递归 n-1 的话，复杂度为 O(n)，会超出递归限制。故对 n/2 进行递归，复杂度可控制在 O(log n)
另外，对n进行位运算并未发现可以提高效率
"""


# 解法-递归
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            x = 1.0 / x
            n = -n

        if n % 2:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, -10))

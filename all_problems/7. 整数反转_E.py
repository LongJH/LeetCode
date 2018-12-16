#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
7. 整数反转
"""

"""
题目：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


"""
解题思路：
1. 使用 flag 记录 x 正负，同时让 x 取绝对值，用 y 记录结果
2. x 依次除 10 并将余数记录到 a ，让 y = 10 * y +a
3. 直到 x == 0，判断 y 是否满足输出条件
"""


class Solution:
    max_num = 2 ** 31
    min_num = - 2 ** 31 + 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """执行用时: 68 ms, 在Reverse Integer的Python3提交中击败了81.56% 的用户"""
        flag = 1    # 记录正负
        y = 0       # 记录结果

        if x < 0:   # 负数取反
            flag = -1
            x = -x

        while x:    # 当 x>0
            a = x % 10  # 当前 x 个位数
            y = y * 10 + a
            x = x // 10

        y *= flag
        if y > self.max_num or y < self.min_num:
            return 0

        return y


"""
解题思路：
偷懒方法，数字转换字符串取逆序再转换为数字
"""


class Solution:
    max_num = 2 ** 31
    min_num = - 2 ** 31 + 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """执行用时: 68 ms, 在Reverse Integer的Python3提交中击败了81.56% 的用户"""
        if x > self.max_num or x < self.min_num:
            return 0

        s = str(x)
        if x < 0:
            s = s[1:]
            r = - int(s[::-1])
            return r if r > self.min_num else 0

        r = int(s[::-1])
        return r if r < self.max_num else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-14236469))
    2**31

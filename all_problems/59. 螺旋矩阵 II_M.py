#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
59. 螺旋矩阵 II
"""

"""
题目：
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

"""
思路1：
参考 54.螺旋矩阵
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        """执行用时: 52 ms, 在Spiral Matrix II的Python3提交中击败了46.26% 的用户"""

        res = [[0 for i in range(n)] for j in range(n)]
        num = 1

        i = j = 0

        ti = 0
        bi = n
        lj = 0
        rj = n

        while 1:
            for j in range(lj, rj):         # 从左到右
                res[i][j] = num
                num += 1
            ti += 1
            if ti == bi:
                break

            for i in range(ti, bi):         # 从上到下
                res[i][j] = num
                num += 1
            rj -= 1
            if lj == rj:
                break

            for j in range(rj - 1, lj - 1, -1):         # 从右到左
                res[i][j] = num
                num += 1
            bi -= 1
            if ti == bi:
                break

            for i in range(bi - 1, ti - 1, -1):         # 从下到上
                res[i][j] = num
                num += 1
            lj += 1
            if lj == rj:
                break

        return res


if __name__ == '__main__':
    slt = Solution()
    print(slt.generateMatrix(3))

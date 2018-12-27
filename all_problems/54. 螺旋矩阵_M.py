#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
54. 螺旋矩阵
"""

"""
题目：
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""
思路1：
用 i，j 作为位置指标，从最外层到最里层遍历元素
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """执行用时: 44 ms, 在Spiral Matrix的Python3提交中击败了77.64% 的用户"""
        if not matrix:
            return []

        di = len(matrix)
        dj = len(matrix[0])

        i = j = 0

        res = []

        ti = 0
        bi = di
        lj = 0
        rj = dj

        while 1:
            for j in range(lj, rj):         # 从左到右
                res.append(matrix[i][j])
            ti += 1
            if ti == bi:
                break

            for i in range(ti, bi):         # 从上到下
                res.append(matrix[i][j])
            rj -= 1
            if lj == rj:
                break

            for j in range(rj - 1, lj - 1, -1):         # 从右到左
                res.append(matrix[i][j])
            bi -= 1
            if ti == bi:
                break

            for i in range(bi - 1, ti - 1, -1):         # 从下到上
                res.append(matrix[i][j])
            lj += 1
            if lj == rj:
                break

        return res

if __name__ == '__main__':
    slt = Solution()
    matrix = [

]
    print(slt.spiralOrder(matrix))

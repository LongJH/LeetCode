#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
74. 搜索二维矩阵
"""

"""
题目：
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""

"""
思路：
使用二分法查找, 复杂度 O(log(m + n))
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """执行用时: 44 ms, 在Search a 2D Matrix的Python3提交中击败了99.33% 的用户 """

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        # 找到第k行
        i, j = 0, m - 1
        if matrix[i][0] == target or matrix[j][0] == target:
            return True

        if matrix[j][0] > target:
            while i < j - 1:
                k = (i + j) // 2
                if matrix[k][0] == target:
                    return True

                if matrix[k][0] > target:
                    j = k
                else:
                    i = k
            k1 = i
        else:
            k1 = j

        i, j = 0, n - 1
        if matrix[k1][i] == target or matrix[k1][j] == target:
            return True

        while i < j - 1:
            k = (i + j) // 2
            if matrix[k1][k] == target:
                return True

            if matrix[k1][k] > target:
                j = k
            else:
                i = k

        return False


if __name__ == '__main__':
    slt = Solution()
    matrix = [
        [1],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(slt.searchMatrix(matrix, 50))
    matrix

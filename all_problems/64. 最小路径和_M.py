#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
64. 最小路径和
"""

"""
题目：
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
解题思路：
参考 62.不同路径 思路2
当前元素 p[i][j] = min(p[i][j - 1], p[i - 1][j]) + w[i][j]
"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """执行用时: 72 ms, 在Minimum Path Sum的Python3提交中击败了72.53% 的用户"""
        m, n = len(grid), len(grid[0])
        matrix = [[0 for j in range(n)] for i in range(m)]
        # matrix = [[0] * n] * m

        for j in range(n):
            for i in range(m):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                    continue

                if i == 0:
                    matrix[i][j] = matrix[i][j - 1] + grid[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] + grid[i][j]
                else:
                    matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j]) + grid[i][j]
        return matrix[-1][-1]


"""
解题思路：
同上
"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """执行用时: 72 ms, 在Minimum Path Sum的Python3提交中击败了72.53% 的用户"""
        m, n = len(grid), len(grid[0])
        matrix = [[0 for j in range(n)] for i in range(m)]
        # matrix = [[0] * n] * m

        matrix[0][0] = grid[0][0]
        for i in range(1, m):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]
        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]

        for j in range(1, n):
            for i in range(1, m):
                matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j]) + grid[i][j]

        return matrix[-1][-1]


if __name__ == '__main__':
    slt = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(slt.minPathSum(grid))

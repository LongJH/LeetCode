#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
63. 不同路径 II
"""

"""
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

"""
解题思路：
参考 62.不同路径 思路2
矩阵的第一行与第一列均为1，表示到该点的路径，其中每个元素均等于其上一个元素与左边元素的和
若原矩阵中是障碍物，则当前值设为 0
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """执行用时: 44 ms, 在Unique Paths II的Python3提交中击败了99.41% 的用户"""
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0 for j in range(n)] for i in range(m)]
        # matrix = [[0] * n] * m

        for j in range(n):
            for i in range(m):
                if obstacleGrid[i][j]:
                    matrix[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    matrix[i][j] = 1
                    continue

                if i == 0:
                    matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
        return matrix[-1][-1]


if __name__ == '__main__':
    slt = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[1,0,0],[0,0,0]]
    print(slt.uniquePathsWithObstacles(obstacleGrid))

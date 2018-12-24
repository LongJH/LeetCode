#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
48. 旋转图像
"""

"""
题目：
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

"""
思路1：
从最外一层到最里一层依次旋转，每次旋转对应4个元素，对应关系为：
    di,dj,      dj,dim - di - 1,     dim - di - 1,dim - dj - 1,         dim - dj - 1,di,
      ↓                ↓                        ↓                           ↓
dim - dj - 1,di,     di,dj,             dj,dim - di - 1,        dim - di - 1,dim - dj - 1,    
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """执行用时: 44 ms, 在Rotate Image的Python3提交中击败了99.53% 的用户"""
        dim = len(matrix)
        # 从最外一层到最里一层旋转
        for di in range(dim // 2):
            for dj in range((dim + 1) // 2):
                matrix[di][dj], matrix[dj][dim - di - 1], matrix[dim - di - 1][dim - dj - 1], matrix[dim - dj - 1][di] = \
                    matrix[dim - dj - 1][di], matrix[di][dj], matrix[dj][dim - di - 1], matrix[dim - di - 1][dim - dj - 1],
                # print(matrix)
        return


if __name__ == '__main__':
    slt = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    slt.rotate(matrix)
    matrix

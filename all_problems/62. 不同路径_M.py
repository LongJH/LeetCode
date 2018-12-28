#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
61. 旋转链表
"""

"""
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""

"""
解题思路：
先判断长宽为 m，n，若 m = 1，则路线 p = 1, 若 m = 2， p = m (sum(1 for i in m), 每增加一层都是对上一层路线的求和
使用递归实现。
当 m，n 较大时，递归时间太长，预计会超出时间限制
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = (m, n) if m >= n else (n, m)
        return self.calPaths(m, n)

    def calPaths(self, m, n):
        if n == 1:
            return 1
        if n == 2:
            return m

        return sum([self.calPaths(i, n - 1) for i in range(1, m + 1)])


"""
解题思路2：
矩阵的第一行与第一列均为1，表示到该点的路径，其中每个元素均等于其上一个元素与左边元素的和
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """执行用时: 52 ms, 在Unique Paths的Python3提交中击败了40.08% 的用户"""
        matrix = [[0 for j in range(m)] for i in range(n)]

        for j in range(m):
            for i in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
                print(i, j, matrix[i][j])
        print(matrix)
        return matrix[-1][-1]


"""
解题思路3：
使用组合的思路，机器人实际走了 m+n-2, 其中 n-1 步往下走，所以走法是 C(n-1, m+n-2)
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """执行用时: 40 ms, 在Unique Paths的Python3提交中击败了99.69% 的用户"""
        a = m + n - 2
        b = (m - 1) if m < n else (n - 1)

        print(a, b)
        res = 1
        for i in range(b - 1, -1, -1):
            res = res * (a - i) // (b - i)

        return res


if __name__ == '__main__':
    slt = Solution()
    print(slt.uniquePaths(4, 6))

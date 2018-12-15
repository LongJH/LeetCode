#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
107. 二叉树的层次遍历 II
"""

from structure.tree_node import *

"""
题目：
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如:

给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [15,7],
  [9,20],
  [3]
]
"""

"""
解题思路：
1. 参考 102，最终返回 order 逆序
"""


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        order = []
        this_level = [root]
        while this_level:
            this_level_order = []
            next_level = []

            while this_level:  # this_level 或 nxt_level 非空
                # 遍历当前 level 并记录左右结点
                node = this_level.pop(0)  # 弹出首个结点
                this_level_order.append(node.val)
                # 记录左右结点
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # 将 当前层的序 添加到 order
            order.append(this_level_order)
            this_level = next_level

        return order[::-1]


if __name__ == '__main__':
    s = Solution()
    node = stringToTreeNode("[3,9,20,null,null,15,7]")
    prettyPrintTree(node)
    s.levelOrder(node)
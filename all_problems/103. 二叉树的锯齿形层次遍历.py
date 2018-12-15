#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
103. 二叉树的锯齿形层次遍历
"""

from structure.tree_node import *

"""
题目：
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如:

给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""

"""
解题思路：
1. 参考 102，添加 level_i 插入对层数进行判断
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
        level_i = 0
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
            order.append(this_level_order if level_i % 2 == 0 else this_level_order[::-1])
            this_level = next_level
            level_i += 1

        return order


if __name__ == '__main__':
    s = Solution()
    node = stringToTreeNode("[3,9,20,null,null,15,7]")
    prettyPrintTree(node)
    s.levelOrder(node)


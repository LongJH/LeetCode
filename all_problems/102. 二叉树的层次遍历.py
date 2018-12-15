#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
102. 二叉树的层次遍历
"""

from structure.tree_node import *

"""
题目：
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

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
  [9,20],
  [15,7]
]
"""

"""
解题思路：
1. 对每一层构建一个队列 this_level，逐个元素弹出时记录值到 this_level_order，并将左右子结点添加到下一层的队列 next_level
2. 若 this_level 中已经没有元素（已完成遍历），则将 this_level_order 添加到 order，并使 this_level = next_level 开始遍历下一层
3. 直到全部元素完成遍历
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

            order.append(this_level_order)  # 将 当前层的序 添加到 order
            this_level = next_level

        return order


if __name__ == '__main__':
    s = Solution()
    node = stringToTreeNode("[3,9,20,null,null,15,7]")
    prettyPrintTree(node)
    s.levelOrder(node)

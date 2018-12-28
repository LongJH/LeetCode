#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
61. 旋转链表
"""

from structure.list_node import *

"""
题目：
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""

"""
解题思路：
关键找到倒数第k个元素, 由于 k 可能大于链表长度，此时需要从头开始重复查找
"""



class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """超出时间限制"""
        if not head or not head.next:
            return head

        h = ListNode(-1)
        h.next = head

        d = h       # 指向当前
        f = h       # 指向 k 之后
        for i in range(k):
            f = f.next
            if not f:       # 超出长度重新查找
                f = h.next

        # 若 f 是最后一个元素，直接返回
        if not f.next:
            return h.next

        while f.next:      # 找到倒数第k个元素
            f = f.next
            d = d.next

        f.next = h.next
        h.next = d.next
        d.next = None

        return h.next


"""
解题思路：
第一次遍历确定链表长度，第二次遍历找到目标元素然后修改链表。
"""


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """执行用时: 60 ms, 在Rotate List的Python3提交中击败了73.68% 的用户"""
        if not head or not head.next:
            return head

        h = ListNode(-1)
        h.next = head

        d = h       # 指向当前
        f = h       # 指向 k 之后
        len_node = 0

        # 第一次遍历确定链表长度, 最后 f 指向最后一个元素
        while f.next:
            len_node += 1
            f = f.next

        # 确定偏移量
        k2 = len_node - k % len_node

        if k2 == len_node or k2 == 0:
            return h.next

        # 第二次遍历，找到更改后的开头元素
        for i in range(k2):
            d = d.next

        f.next = h.next
        h.next = d.next
        d.next = None

        return h.next


if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.rotateRight(node, 2000000))
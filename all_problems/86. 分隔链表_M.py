#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
86. 分隔链表
"""

from structure.list_node import *

"""
题目：
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

"""
解题思路：

"""


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        """执行用时: 60 ms, 在Partition List的Python3提交中击败了46.33% 的用户"""
        cur1 = l1 = ListNode(-1)
        cur2 = l2 = ListNode(-1)

        cur = head

        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next

            cur = cur.next

        cur1.next = l2.next
        cur2.next = None

        return l1.next

if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1,4,3,2,5,2]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.partition(node, 4))

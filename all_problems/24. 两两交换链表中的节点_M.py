#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
24. 两两交换链表中的节点
"""

from structure.list_node import *

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

"""
解题思路：

"""


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """执行用时: 48 ms, 在Swap Nodes in Pairs的Python3提交中击败了65.40% 的用户"""
        h = ListNode(-1)
        h.next = head
        cur = h

        while cur.next and cur.next.next:
            n1, n2, n3 = cur.next, cur.next.next, cur.next.next.next
            # cur.next, cur.next.next, cur.next.next.next = cur.next.next, cur.next.next.next, cur.next
            cur.next, n1.next, n2.next = n2, n3, n1
            cur = cur.next.next

        return h.next

if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3, 4, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.swapPairs(node))

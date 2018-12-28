#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
19. 删除链表的倒数第N个节点
"""

from structure.list_node import *

"""
题目：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""

"""
解题思路：
使用双指针，一个f指向head，一个s指向n个以后，两者同时往后遍历，当s为空时表示f为倒数第n个元素
"""


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """执行用时: 48 ms, 在Remove Nth Node From End of List的Python3提交中击败了99.70% 的用户 """
        h = ListNode(-1)
        h.next = head

        d = h
        f = h
        for i in range(n):
            f = f.next

        while f.next:
            f = f.next
            d = d.next

        d.next = d.next.next

        return h.next


if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3, 4, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.removeNthFromEnd(node, 5))

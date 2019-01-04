#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
82. 删除排序链表中的重复元素 II
"""

from structure.list_node import *

"""
题目：
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""

"""
解题思路：
判断当前结点与下一个结点值是否一样，若一样，则记录上一结点，并指向下一个不重复的元素
"""


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """执行用时: 72 ms, 在Remove Duplicates from Sorted List II的Python3提交中击败了46.92% 的用户"""
        h = ListNode(-1)
        h.next = head

        cur = h

        while cur.next:
            if cur.next.next and cur.next.val == cur.next.next.val:
                last = cur
                cur = cur.next
                while cur.next.next and cur.next.val == cur.next.next.val:
                    cur = cur.next

                last.next = cur.next.next
                cur = last
                continue

            cur = cur.next

        return h.next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """执行用时: 56 ms, 在Remove Duplicates from Sorted List II的Python3提交中击败了99.12% 的用户"""
        h = ListNode(-1)
        h.next = head

        last, cur = h, head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if last.next == cur:
                last = cur
            else:
                last.next = cur.next

            cur = cur.next

        return h.next

if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.deleteDuplicates(node))

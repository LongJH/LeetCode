#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
83. 删除排序链表中的重复元素
"""

from structure.list_node import *

"""
题目：
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""

"""
解题思路：

"""


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """执行用时: 56 ms, 在Remove Duplicates from Sorted List的Python3提交中击败了99.73% 的用户"""
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
                continue

            cur = cur.next

        return head

if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.deleteDuplicates(node))

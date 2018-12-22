#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
21. 合并两个有序链表
"""

from structure.list_node import *

"""
题目：
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

"""
插入排序：
时间复杂度在O(nlogN)的排序算法是快速排序，堆排序，归并排序。
但是快排的最坏时间复杂度是O(n^2), 平均时间复杂度为O(nlogn)，所以不考虑快速排序。而堆排序太繁琐了。
对于数组来说占用的空间复杂度分别为O(1),O(n),O(n)。但是对于链表来说使用归并排序占用空间为O(1)。
"""


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """执行用时: 72 ms, 在Merge Two Sorted Lists的Python3提交中击败了28.51% 的用户 """
        cur = h = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return h.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [3, 3, 4]
    s = Solution()
    l1 = stringToListNode(str(l1))
    l2 = stringToListNode(str(l2))
    # prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.mergeTwoLists(l1, l2))


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
148. 排序链表
"""

from structure.list_node import *

"""
题目：
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入:  4->2->1->3
输出:  1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

"""
插入排序：
时间复杂度在O(nlogN)的排序算法是快速排序，堆排序，归并排序。
但是快排的最坏时间复杂度是O(n^2), 平均时间复杂度为O(nlogn)，所以不考虑快速排序。而堆排序太繁琐了。
对于数组来说占用的空间复杂度分别为O(1),O(n),O(n)。但是对于链表来说使用归并排序占用空间为O(1)。
"""


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 找出中间结点
        mid = self.get_mid(head)

        # 切分两个链表
        l = head
        r = mid.next
        mid.next = None

        # 递归进行有序链表合并
        return self.merge(self.sortList(l), self.sortList(r))

    def get_mid(self, node):
        # 使用快慢指针找到中间结点
        if not node:
            return node

        fast = slow = node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, p, q):
        # 合并两个有序链表
        h = ListNode(-1)
        cur = h
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        if p:
            cur.next = p
        if q:
            cur.next = q

        return h.next


if __name__ == '__main__':
    l = [7, 6, 8, 9, 1, 5]
    s = Solution()
    node = stringToListNode(str(l))
    # prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.sortList(node))

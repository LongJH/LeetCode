#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
2. 两数相加
"""

from structure.list_node import *

"""
题目：
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

"""
思路：
1. 同时遍历两个链表元素，若相加大于10，则保存其个位数，并使 进位符carry=1，添加到下一个元素的和中
2. 若某一个链表已完成遍历，继续遍历链表
"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """执行用时: 132 ms, 在Add Two Numbers的Python3提交中击败了95.48% 的用户"""
        p = l1
        q = l2
        h = ListNode(-1)
        cur = h

        carry = 0

        while p and q:
            sum_val = p.val + q.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            p = p.next
            q = q.next

        while p:
            sum_val = p.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            p = p.next

        while q:
            sum_val = q.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            q = q.next

        if carry:
            cur.next = ListNode(carry)

        return h.next


"""
思路2（效果不好）：
原理同上，但当某一个链表完成遍历后，若 carry 为0，则让剩余部分指向另一个链表
"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """执行用时: 220 ms, 在Add Two Numbers的Python3提交中击败了10.36% 的用户 """
        p = l1
        q = l2
        h = ListNode(-1)
        cur = h

        carry = 0

        while p and q:
            sum_val = p.val + q.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            p = p.next
            q = q.next

        while p:
            if not carry:
                cur.next = p
                break

            sum_val = p.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            p = p.next

        while q:
            if not carry:
                cur.next = q
                break

            sum_val = q.val + carry
            carry = 0

            if sum_val >= 10:
                sum_val = sum_val - 10
                carry = 1

            cur.next = ListNode(sum_val)
            cur = cur.next
            q = q.next

        if carry:
            cur.next = ListNode(carry)

        return h.next


if __name__ == '__main__':
    s = Solution()
    node1 = stringToListNode(str([1, 2, 3, 4, 5]))
    node2 = stringToListNode(str([1, 2, 3, 4, 5, 6, 7, 8, 9, ]))
    prettyPrintLinkedList(node1)
    prettyPrintLinkedList(node2)
    prettyPrintLinkedList(s.addTwoNumbers(node1, node2))

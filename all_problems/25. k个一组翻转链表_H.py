#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
25. k个一组翻转链表
"""

from structure.list_node import *

"""
题目：
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

"""
解题思路：
使用 k_next 指向 k个以后的元素，并将中间元素进行反转。
具体方法参考 92. 反转链表 II
"""


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """执行用时: 68 ms, 在Reverse Nodes in k-Group的Python3提交中击败了98.42% 的用户 """
        cur = h = ListNode(-1)
        h.next = k_next = head

        while cur.next and k_next:
            # 寻找 k 个后元素或结尾
            for i in range(k):
                if k_next:
                    k_next = k_next.next
                else:
                    return h.next

            # 反转链表
            fst = p = cur.next
            q = p.next
            while q != k_next:
                n = q.next
                q.next = p
                p, q = q, n

            cur.next, fst.next = p, k_next

            cur = fst

        return h.next

if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3, 4, 5]))
    prettyPrintLinkedList(node)
    r = s.reverseKGroup(node, 4)
    prettyPrintLinkedList(r)


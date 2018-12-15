#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
92. 反转链表 II
"""

from structure.list_node import *

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明: 1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

"""
解题思路：
1. 获取当前指针 this_node 与上一个指针 last_node（当头指针指向this_node时，last_node为None）
2. 记录下一个指针 next_node
3. 修改 this_node 指向元素 this_node->last_node
4. 往后遍历元素，使得 this_node = next_node
5. 直到 this_node 为空，则 last_node 为反转链表的头指针
"""


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 创建一个空的头指针，指向 head
        head_node = ListNode(-1)
        head_node.next = head

        last_node = head_node
        this_node = head_node.next
        i = 1
        while this_node:  # 获取当前指针
            next_node = this_node.next  # 记录下一个node
            if i == m:  # 反转开始
                # 记录上一个结点与当前结点
                pre = last_node
                fst = this_node

            if i - 1 >= m and i <= n:  # 当前元素在需反转的链表内
                this_node.next = last_node  # 修改指针

            if i == n:  # 反转结束
                # 修改指针
                pre.next = this_node
                fst.next = next_node

            # 往后遍历
            last_node, this_node = this_node, next_node
            i += 1

        return head_node.next


if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3, 4, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.reverseBetween(node, 2, 4))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
206. 反转链表
"""

from structure.list_node import *

"""
题目：
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

"""
解题思路1-常规解法：
1. 获取当前指针 this_node 与上一个指针 last_node（当头指针指向this_node时，last_node为None）
2. 记录下一个指针 next_node
3. 修改 this_node 指向元素 this_node->last_node
4. 往后遍历元素，使得 this_node = next_node
5. 直到 this_node 为空，则 last_node 为反转链表的头指针
"""


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_node = None
        this_node = head
        while this_node:  # 获取当前指针
            next_node = this_node.next  # 记录下一个node
            this_node.next = last_node  # 修改指针
            last_node, this_node = this_node, next_node  # 往后遍历

        return last_node


"""
解题思路2-递归：
1. 若当前元素的 next 非空，则反转 next 对应的链表，并将链表中第一个元素的 next 指向本元素，并将本元素的 next 指向空（本元素为链表结束）
2. 若 next 为空，返回本身
"""


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            next_node = head.next
            rl = self.reverseList(next_node)
            next_node.next = head
            head.next = None
            return rl

        return head


if __name__ == '__main__':
    s = Solution()
    node = stringToListNode(str([1, 2, 3, 4, 5]))
    prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.reverseList(node))

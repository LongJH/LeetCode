#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
147. 对链表进行插入排序
"""

from structure.list_node import *

"""
题目：
对链表进行插入排序
从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，
找到它在序列中适当的位置，并将其插入。 重复直到所有输入数据插入完为止。

示例 1:
输入:  4->2->1->3
输出:  1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

"""
插入排序：
1. 将指针指向某个元素，假设该元素左侧的元素全部有序，将该元素抽取出来，然后按照从右往左的顺序分别与其左边的元素比较，
   遇到比其大的元素便将元素右移，直到找到比该元素小的元素或者找到最左面发现其左侧的元素都比它大，停止；
2. 此时会出现一个空位，将该元素放入到空位中，此时该元素左侧的元素都比它小，右侧的元素都比它大；
3. 指针向后移动一位，重复上述过程。每操作一轮，左侧有序元素都增加一个，右侧无序元素都减少一个。
"""


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        # 创建一个空的头指针，指向 head
        head_node = ListNode(-999999)
        head_node.next = head

        cur_node = head
        while cur_node.next:
            p_node = cur_node.next  # 指向需要被比较的结点
            f_node = head_node  # 指向该结点之前，已排序好的链表
            while f_node != cur_node:
                if p_node.val < f_node.next.val:
                    # 交换位置
                    f_node.next, p_node.next, cur_node.next = p_node, f_node.next, p_node.next
                    break
                else:
                    f_node = f_node.next
            if f_node == cur_node:  # 若没有元素没有移动位置，则遍历下一个元素
                cur_node = cur_node.next

        return head_node.next


if __name__ == '__main__':
    l = [7, 6, 8, 9, 1, 5]
    s = Solution()
    node = stringToListNode(str(l))
    # prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.insertionSortList(node))

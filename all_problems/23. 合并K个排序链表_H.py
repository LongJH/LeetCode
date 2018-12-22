#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
23. 合并K个排序链表
"""

from structure.list_node import *

"""
题目：
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""

"""
思路：
以第1个列表为基础，与逐个与后面链表合并，时间复杂度 O(n^2)
"""


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """超出时间限制"""

        if not lists:
            return
        cur = lists[0]
        for l in lists[1:]:
            cur = self.mergeTwoLists(cur, l)

        return cur

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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


"""
思路2：
两两合并
"""


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """执行用时: 180 ms, 在Merge k Sorted Lists的Python3提交中击败了34.02% 的用户"""

        if not lists:
            return

        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists) // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists.pop(i + 1))

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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


"""
思路3：
使用堆，构建一个长度为k的堆, 存放 k 个列表的首元素。依次抛出堆中的最小元素，并让其列表的下一个元素入堆。
因为入堆的复杂度为 logk，
由于python3的heapq中对元组进行比较时，如果第一个元素比较结果相同，则会比较下一个元素，即比较ListNode从而抛出异常。针对这个问题，我们在元组中增加一个 x 来解决，这个x表示当前是第几个列表
"""
import heapq

class Solution:
    import heapq

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """执行用时: 96 ms, 在Merge k Sorted Lists的Python3提交中击败了90.74% 的用户 """

        res = ListNode(-1)
        cur = res
        p = list()

        x = 0
        for i in lists:
            if i:
                heapq.heappush(p, (i.val, x, i))
                x += 1

        while len(p) > 0:
            cur_x, cur.next = heapq.heappop(p)[1:]
            cur = cur.next

            if cur.next:
                heapq.heappush(p, (cur.next.val, cur_x, cur.next))

        return res.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [3, 3, 4]
    s = Solution()
    l1 = stringToListNode(str(l1))
    l2 = stringToListNode(str(l2))
    # prettyPrintLinkedList(node)
    prettyPrintLinkedList(s.mergeKLists([l1, l2]))


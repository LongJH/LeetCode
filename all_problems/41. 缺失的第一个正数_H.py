#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
40. 组合总和 II
"""

"""
题目：
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""

"""
解题思路：
本题的难点在于只能使用常数级别的空间，也就是说，不能开辟一个flag数组，若出现某个数，就将flag值标1，最后看flag数组第一个为0的下标。本题的思路是从前往后将数放到它正确的位置上去。
第一次遍历，将元元素放置到对应的各自中，如 当前数字是 3，而 nums[3-1] != 3, 则将 3 与 nums[3-1] 的元素交换。
第二次遍历，如果发现 i+1 != nums[i] 则表示当前元素缺失，返回 i+1, 否则返回 len
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """执行用时: 44 ms, 在First Missing Positive的Python3提交中击败了99.50% 的用户"""
        # 第一次遍历， 将元元素放置到对应的各自中
        len_n = len(nums)
        i = 0
        while i < len_n:
            if nums[i] > len_n or nums[i] <= 0:
                i += 1
                continue
            if i + 1 != nums[i]:
                j = nums[i] - 1     # nums[i] 应该所在的位置
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    continue
            i += 1

        # 第二次遍历，寻找第一个 <= 0 的元素
        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        return len_n + 1

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1,1]))
